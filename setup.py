# -*- coding: utf-8 -*-
# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-10T21:42:57+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: setup.py
# @Last modified by:   developer
# @Last modified time: 2019-01-24T10:42:18+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri

from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

version = '0.0.1'

setup(
	name='awesome_cart',
	version=version,
	description='Razorpay Payment Gateway Integration',
	author='Frappe Technologies Pvt. Ltd.',
	author_email='info@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
