# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:21:33 2020

@author: Dell
"""

from pygdrive3 import service

drive_service = service.DriveService('./client_secrets.json')
drive_service.auth()

#folder = drive_service.create_folder('tryupload')
file = drive_service.upload_file('Pydrive', './main.py', 'tryupload')
link = drive_service.anyone_permission(file)

#folders = drive_service.list_folders_by_name('tryupload')
#files = drive_service.list_files_by_name('Arquivo Teste')

#files_from_folder = drive_service.list_files_from_folder_id(folder)`