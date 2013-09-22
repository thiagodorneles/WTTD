# coding: utf-8
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Thiago Dorneles',
            cpf='12345678901',
            email='thiagodornelesrs@gmail.com',
            phone='51 9246.5987'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Thiago Dorneles', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Thiago Dorneles',
                                    cpf='12345678901',
                                    email='thiagodornelesrs@gmail.com',
                                    phone='51 9246.5987')
    def test_cpf_unique(self):
        'CPF should be unique'
        s = Subscription(name='Thiago Dorneles',
                        cpf='12345678901',
                        email='outro@mail.com',
                        phone='51 9246.5987')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email should be unique'
        s = Subscription(name='Thiago Dorneles',
                        cpf='00000000000',
                        email='thiagodornelesrs@gmail.com',
                        phone='51 9246.5987')
        self.assertRaises(IntegrityError, s.save)