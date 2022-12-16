#!/usr/bin/env python

"""Tests for `pavilion_cms` package."""

import requests

# from pavilion_cms import pavilion_cms
from pavilion_cms import PavilionCMS

from .fixtures import ALL_CATEGORIES, ALL_TAGS


def test_get_all_tags(mocker):
    pav_cms = PavilionCMS("test_token")
    response = requests.Response()
    response.status_code = 200

    requests_mock = mocker.patch.object(response, "json", return_value=ALL_TAGS)
    pav_object = mocker.patch.object(pav_cms._session, "get", return_value=response)

    resp = pav_cms.get_all_tags()

    assert resp is not None
    assert resp["metadata"]["total_pages"] == 1
    assert resp["metadata"]["count"] == 5
    assert len(resp["results"]) == 5

    requests_mock.assert_called()
    pav_object.assert_called_once()


def test_get_single_tag(mocker):
    pav_cms = PavilionCMS("test_token")
    response = requests.Response()
    response.status_code = 200

    requests_mock = mocker.patch.object(
        response, "json", return_value=ALL_TAGS["results"][0]
    )
    mocker.patch.object(pav_cms._session, "get", return_value=response)

    resp = pav_cms.get_tag(ALL_TAGS["results"][0]["id"])

    assert resp is not None
    assert resp["id"] == ALL_TAGS["results"][0]["id"]
    assert resp["name"] == ALL_TAGS["results"][0]["name"]

    requests_mock.assert_called()


def test_get_all_categories(mocker):
    pav_cms = PavilionCMS("test_token")
    response = requests.Response()
    response.status_code = 200

    requests_mock = mocker.patch.object(response, "json", return_value=ALL_CATEGORIES)
    pav_object = mocker.patch.object(pav_cms._session, "get", return_value=response)

    resp = pav_cms.get_all_categories()

    assert resp is not None
    assert resp["metadata"]["total_pages"] == 1
    assert resp["metadata"]["count"] == 4
    assert len(resp["results"]) == 4

    requests_mock.assert_called()
    pav_object.assert_called_once()


def test_get_single_category(mocker):
    pav_cms = PavilionCMS("test_token")
    response = requests.Response()
    response.status_code = 200

    requests_mock = mocker.patch.object(
        response, "json", return_value=ALL_CATEGORIES["results"][0]
    )
    mocker.patch.object(pav_cms._session, "get", return_value=response)

    resp = pav_cms.get_category(ALL_CATEGORIES["results"][0]["id"])

    assert resp is not None
    assert resp["id"] == ALL_CATEGORIES["results"][0]["id"]
    assert resp["name"] == ALL_CATEGORIES["results"][0]["name"]

    requests_mock.assert_called()
