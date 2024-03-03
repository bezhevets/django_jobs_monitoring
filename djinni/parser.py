from datetime import datetime
from pprint import pprint
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from pytz import timezone

from djinni.models import VacancyDjinni

BASE_URL = "https://djinni.co/"


def detail_vacancy(url: str):
    page = requests.get(urljoin(BASE_URL, url)).content
    soup = BeautifulSoup(page, "html.parser")

    additional_info = soup.select(".job-additional-info--body")

    description = soup.select_one(".row-mobile-order-2 > .mb-4").text.strip()
    english = " ".join(
        additional_info[0]
        .select(".job-additional-info--item")[-2]
        .text.split()[1:]
    )
    experience = (
        additional_info[0]
        .select(".job-additional-info--item")[-1]
        .text.strip()
    )
    employment_type = (
        additional_info[1]
        .find("span", "bi-building")
        .find_next("div")
        .text.strip()
    )
    return dict(
        description=description,
        english=english,
        experience=experience,
        employment_type=employment_type,
    )

    # pprint(dict(employment_type=soup.select_one(".job-additional-info--item-text").text,
    #             experience=soup.select_one(".job-additional-info--item-text")))


def get_correct_time(time: str) -> datetime:
    print(time)
    naive_datetime = datetime.strptime(time, "%H:%M %d.%m.%Y")
    print(naive_datetime)
    kiev_datetime = timezone("Europe/Kiev").localize(naive_datetime)
    print(kiev_datetime)
    return kiev_datetime


def single_vacancy(vacancy_soup: BeautifulSoup):
    info = dict(
        title=vacancy_soup.select_one(".job-list-item__link").text.strip(),
        intro=vacancy_soup.select_one(".job-list-item__description > span")
        .text.replace("\r\n", "")
        .strip(),
        company=vacancy_soup.select_one("a.mr-2").text.strip(),
        location=" ".join(
            vacancy_soup.select_one(".location-text").text.split()
        ),
        date=get_correct_time(
            vacancy_soup.select_one(
                "div.job-list-item__counts > .text-muted > .mr-2.nobr"
            )["title"]
        ),
        reviews=int(
            vacancy_soup.select_one(".text-muted")
            .select(".mr-2")[-1]["title"]
            .split()[0]
        ),
        url=urljoin(
            BASE_URL, vacancy_soup.select_one(".job-list-item__link")["href"]
        ),
    )
    info.update(
        detail_vacancy(vacancy_soup.select_one(".job-list-item__link")["href"])
    )
    return info


def parser_list_vacancies():
    page = requests.get(
        urljoin(BASE_URL, "jobs/?primary_keyword=Python")
    ).content
    soup = BeautifulSoup(page, "html.parser")

    vacancies = soup.select(".job-list__item")
    for vacancy in vacancies[:2]:
        dict_v = single_vacancy(vacancy)
        pprint(dict_v)
        vac = VacancyDjinni(**dict_v)
        try:
            vac.save()
        except:
            continue
