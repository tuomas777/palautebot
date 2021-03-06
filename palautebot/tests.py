# -*- coding: utf-8 -*-
from django.test import TestCase
from palautebot.models import Feedback
from django.core.management.base import BaseCommand
from palautebot.management.commands.palautebot import Command
from django.db import connection
import datetime
import mock
import pickle
import tweepy


class TestPalautebotTests(TestCase):
    palautebot_cmd = Command()

    def return_true(*args, **kwargs):
        return True

    def mock_twitter_search(search_string, rpp=60, since_id=None):
        twitter_response = ''
        with open('src/palautebot/palautebot/test_utilities/test_data_twitter.py', 'rb') as data:
            twitter_response = pickle.load(data)
        return twitter_response

    @mock.patch('palautebot.management.commands.palautebot.Command')
    @mock.patch('palautebot.management.commands.palautebot.Command.answer_to_tweet', side_effect=return_true)
    @mock.patch('palautebot.management.commands.palautebot.tweepy.API.search', side_effect=mock_twitter_search)
    def test_handle_twitter(self, mock_cmd, mock_answer_to_tweet, mock_twitter_search):
        self.assertEqual(self.palautebot_cmd.handle_twitter(None), [True])

# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2