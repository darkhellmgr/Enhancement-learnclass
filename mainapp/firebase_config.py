import re
from datetime import date, datetime

import pyrebase
from django import forms
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from mainapp.forms import SchoolModelForm, StudentForm, ParentForm, StaffForm, MyStyleForm, EditSchoolAdminForm, \
    EditStaffForm, EditStudentForm, EditParentForm, EditCourseForm
from mainapp.forms import StudentForm, ParentForm, StaffForm
from mainapp.models import School, Course, User, SchoolAdmin

config = {
    'apiKey': "AIzaSyCkskZ8L8IYap9ss_TvYlJfwYh-tsL5sVg",
    'authDomain': "fs-learnclass.firebaseapp.com",
    'databaseURL': "https://fs-learnclass.firebaseio.com",
    'projectId': "fs-learnclass",
    'storageBucket': "fs-learnclass.appspot.com",
    'messagingSenderId': "495916606300"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()


def gettoken():
    user = authe.current_user
    try:
        token = user['idToken']
        return token
    except:
        pass


def getusernamelist(which, token):
    try:
        data = db.child("Users").get(token).val()
        idlist = list(data[which].keys())
        student_namelist = []
        for i in idlist:
            student_namelist.append(data[which][i]['name'])
        return zip(idlist, student_namelist)
    except:
        pass


def getnameidlist(which, suitablename, token):
    try:
        mydata = db.child(which).get(token).val()
        idslist = list(mydata.keys())
        nameslist = []
        for i in idslist:
            nameslist.append(mydata[i][suitablename])
        return zip(idslist, nameslist)
    except:
        pass


def getform(formtype):
    if formtype == 'Schools':
        modelform = School

    elif formtype == 'SchoolAdmin':
        modelform = SchoolAdmin

    elif formtype == 'Courses':
        modelform = Course

    return (modelform)


def getrelation(which, whichid, node, suitablename, token):
    try:
        data = db.child(which).child(whichid).child(node).get(token).val()
        reverse_data = db.child(node).get(token).val()
        idlist = list(data)
        namelist = []
        for i in idlist:
            namelist.append(reverse_data[i][suitablename])
        return (zip(idlist, namelist))
    except:
        pass


def student_course(uid, token):
    try:
        x = db.child('Users').child('Student').child(uid).child('grade').get(token).val()
        stdcourse = getrelation("Grade", x, 'Courses', 'title', token)
        return stdcourse
    except:
        pass


# for teacher-course
def teacher_relation(uid, node, token):
    try:
        data = db.child('Users').child('Teacher').child(uid).child(node).get(token).val()
        idlist = list(data)
        reverse_data = db.child(node).get(token).val()
        namelist = []
        for i in idlist:
            namelist.append(reverse_data[i]['title'])
        return (zip(idlist, namelist))
    except:
        pass


def getuserid(which, suitablename, token):
    try:
        data = db.child("Users").get(token).val()
        idlist = list(data[which].keys())
        for i in idlist:
            student_gradeid = (data[which][i][suitablename])
        return student_gradeid
    except:
        pass


def getdeadline(which, id, suitablename, token):
    deadline_time = db.child(which).child(id).child(suitablename).get(token).val()
    return deadline_time


def calculate_age(born):
    today = datetime.today()
    print(today)
    print(born)
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age