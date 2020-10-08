#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is the extractLattes script.
#
# Copyright (C) 2020 Rafael Perazzo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author(s): Rafael Perazzo Barbosa Mota <rafael.mota@ufca.edu.br>

import zeep
import zipfile
import os
import logging
import configparser

wsdl = 'https://sci02-ter-jne.ufca.edu.br/cnpq'
client = zeep.Client(wsdl=wsdl)
WORKING_DIR = '/usr/src/app/'
config = configparser.ConfigParser()
config.read(WORKING_DIR + 'config.ini')
XML_DIR = str(config['DEFAULT']['xml_dir'])
IDLATTES_FILE = str(config['DEFAULT']['idlattes_file'])

logging.basicConfig(filename=WORKING_DIR + 'extractor.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s',level=logging.ERROR)

def salvarCV(id):
    resultado = client.service.getCurriculoCompactado(id)
    arquivo = open(id + '.zip','wb')
    arquivo.write(resultado)
    arquivo.close()
    with zipfile.ZipFile(id + '.zip','r') as zip_ref:
        zip_ref.extractall(XML_DIR)
    if os.path.exists(id + '.zip'):
        os.remove(id + '.zip')

ids = open(IDLATTES_FILE,"r").read().splitlines()
for id in ids:
    resultado = client.service.getCurriculoCompactado(id)
    try:
        salvarCV(id)
    except Exception as e:
        logging.error(str(e))