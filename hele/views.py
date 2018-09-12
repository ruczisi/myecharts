from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from pyecharts import Bar,Pie,Grid,Map
from django.template import loader
from hele.models import *


REMOTE_HOST = "https://pyecharts.github.io/assets/js"

def index(request):
    town_list = District.objects.all()
    template = loader.get_template("index.html")
    mymap = Map(width=400)
    attr =["安怀镇","大鹏镇"]
    value = [1,2]
    mymap.add("",attr,value,maptype=u"平南县",is_label_show=True,is_map_symbol_show=True,is_toolbox_show=False )
    context = dict(
        map_myecharts = mymap.render_embed(),
        host = REMOTE_HOST,
        town_list = town_list,
        map_script_list = mymap.get_js_dependencies()
    )
    return HttpResponse(template.render(context,request))

def all_school(request):
    context = dict(
        school_list = School.objects.all(),
        town_list = District.objects.all(),
    )
    return render(request,"hele/school.html",context=context)

def get_school(request,pk):
    town = get_object_or_404(District,pk=pk)
    schools = School.objects.filter(district=town)
    context=dict(
        town_list = District.objects.all(),
        school_town = town,
        school_list = schools
    )
    return render(request,"hele/school.html",context=context)

def myechart(request,pk):
    school = get_object_or_404(Food_Struct,pk=pk)
    school2 = get_object_or_404(School,pk=pk)
    nutri_school = get_object_or_404(Nutri_of_Food,pk=pk)
    students = school2.students
    template = loader.get_template("hele/pyecharts.html")
    mypie = Pie("每人日均餐标结构（单位：%）",title_pos="center")
    value = [school.rice,school.ganhuo,school.cake,school.egg,school.chicken,school.ricenoodle,school.milk,school.beef,school.oil,school.vegitable,school.flavor,school.pock]
    attr = ["大米","干货","糕点","鸡蛋","鸡鸭肉","米粉","奶制品","牛肉","食用油","蔬菜","调味品","猪肉"]
    struct_value = []
    for i in value:
        k = roundfunc(i)
        struct_value.append(k)
    total = roundfunc(school.total)
    mypie.add("",attr,value,is_label_show=True,is_legend_show=False)
    mybar = Bar("每人日均食物摄入结构(单位：g)",title_pos="center")
    nutri_value = [nutri_school.xuqin,nutri_school.fish,nutri_school.soilbean,nutri_school.egg,nutri_school.gushu,nutri_school.milk,nutri_school.sault,nutri_school.vigetable,nutri_school.fruit,nutri_school.oil]
    standart_value = [50,50,40,50,350,200,5,400,250,30]
    nutri_attr = ["畜禽肉","鱼虾类","大豆坚果","蛋类","谷薯类",	"奶制品","食盐","蔬菜类","水果类","植物油"]
    mybar.add("学生实际值",nutri_attr,nutri_value,is_label_show=True,is_legend_show=True,legend_top="bottom")
    mybar.add("标准摄入值",nutri_attr,standart_value,is_label_show=True,is_legend_show=True,legend_top="bottom")
    context = dict(
        school = school,
        town_list = District.objects.all(),
        town = school2.district,
        school_name = school.name.name,
        next_school = next_school(school2.id),
        school_student = students,
        total = total,
        nutr_total=nutri_school.total,
        pie_myecharts = mypie.render_embed(),
        bar_myecharts = mybar.render_embed(),
        host = REMOTE_HOST,
        pie_script_list = mypie.get_js_dependencies(),
        bar_script_list = mybar.get_js_dependencies(),
    )
    return HttpResponse(template.render(context,request))


def roundfunc(k):
    if k == None:
        return 0;
    else:
        return int(int(k*1000+0.5)/10)/100

def label_formatter(params):
    return params.name+":"+params.data+"元"

def next_school(i):
    a = len(list(School.objects.all()))
    if i<a-1:
        return i+1;
    else:
        return 0