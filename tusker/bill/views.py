from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse
from .models import Category, Subcat, Products, Bill
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class Print_obj:
	def __init__(self,qty,tot):
		self.qty = qty
		self.tot = tot
def index(request):
	prod_objs_1 = Products.objects.filter(prod_subcat="1")
	prod_objs_2 = Products.objects.filter(prod_subcat="2")
	prod_objs_3 = Products.objects.filter(prod_subcat="3")
	prod_objs_4 = Products.objects.filter(prod_subcat="4")
	prod_objs_5 = Products.objects.filter(prod_subcat="5")
	prod_objs_6 = Products.objects.filter(prod_subcat="6")
	prod_objs_7 = Products.objects.filter(prod_subcat="7")
	prod_objs_8 = Products.objects.filter(prod_subcat="8")
	prod_objs_9 = Products.objects.filter(prod_subcat="9")
	prod_objs_10 = Products.objects.filter(prod_subcat="10")
	prod_objs_11 = Products.objects.filter(prod_subcat="11")
	prod_objs_12 = Products.objects.filter(prod_subcat="12")
	prod_objs_13 = Products.objects.filter(prod_subcat="13")
	prod_objs_14 = Products.objects.filter(prod_subcat="14")
	prod_objs_15 = Products.objects.filter(prod_subcat="15")
	prod_objs_16 = Products.objects.filter(prod_subcat="16")
	prod_objs_17 = Products.objects.filter(prod_subcat="17")
	prod_objs_18 = Products.objects.filter(prod_subcat="18")
	prod_objs_19 = Products.objects.filter(prod_subcat="19")
	prod_objs_20 = Products.objects.filter(prod_subcat="20")
	prod_objs_21 = Products.objects.filter(prod_subcat="21")
	prod_objs_22 = Products.objects.filter(prod_subcat="22")
	prod_objs_23 = Products.objects.filter(prod_subcat="23")
	prod_objs_24 = Products.objects.filter(prod_subcat="24")
	prod_objs_25 = Products.objects.filter(prod_subcat="25")
	prod_objs_26 = Products.objects.filter(prod_subcat="26")
	prod_objs_0 = Products.objects.filter(prod_subcat="0")
	return render(request, 'bill/index.html',{'prod_objs_0':prod_objs_0,'prod_objs_1':prod_objs_1, 'prod_objs_2':prod_objs_2, 'prod_objs_3':prod_objs_3, 'prod_objs_4':prod_objs_4, 'prod_objs_5':prod_objs_5, 'prod_objs_6':prod_objs_6, 'prod_objs_7':prod_objs_7, 'prod_objs_8':prod_objs_8, 'prod_objs_9':prod_objs_9, 'prod_objs_10':prod_objs_10, 'prod_objs_11':prod_objs_11, 'prod_objs_12':prod_objs_12, 'prod_objs_13':prod_objs_13, 'prod_objs_14':prod_objs_14, 'prod_objs_15':prod_objs_15, 'prod_objs_16':prod_objs_16, 'prod_objs_17':prod_objs_17, 'prod_objs_18':prod_objs_18, 'prod_objs_19':prod_objs_19, 'prod_objs_20':prod_objs_20, 'prod_objs_21':prod_objs_21, 'prod_objs_22':prod_objs_22, 'prod_objs_23':prod_objs_23, 'prod_objs_24':prod_objs_24, 'prod_objs_25':prod_objs_25, 'prod_objs_26':prod_objs_26})
def quant(request):
	sel_prod_ids = request.POST.getlist('check[]')
	request.session['sel_prod_ids'] = sel_prod_ids
	t_type_val = request.POST["t_type"]
	b_type_val = request.POST["b_type"]
	request.session['t_type_val'] = t_type_val
	request.session['b_type_val'] = b_type_val
	sel_prod_objs = Products.objects.filter(pk__in=sel_prod_ids)
	if int(t_type_val) == 1:
		return render(request, 'bill/quant.html',{'sel_prod_objs':sel_prod_objs, 't_type_val':t_type_val})
	elif int(t_type_val) == 2:
		return render(request, 'bill/quant.html',{'sel_prod_objs':sel_prod_objs, 't_type_val':t_type_val})
	elif int(t_type_val) == 3:
		return render(request, 'bill/quant.html',{'sel_prod_objs':sel_prod_objs, 't_type_val':t_type_val})
def printp(request):
	sel_prod_ids =request.session['sel_prod_ids']
	t_type_val =request.session['t_type_val']
	sel_prod_objs = Products.objects.filter(pk__in=sel_prod_ids)
	x =  Bill.objects.get(id=1)
	billnum = x.billnum
	request.session['billnum'] = billnum
	x.billnum = x.billnum + 1
	x.save()
	quantity_arr = []
	total_arr =[]
	print_obj_arr = []
	b_type_val = request.session['b_type_val']
	for i in range(1,len(sel_prod_ids)+1):
		quantity = "quant"+str(i)
		total = "total"+str(i)
		quantity_arr.append(request.POST[quantity])
		if int(b_type_val) == 2:
			t = Products.objects.get(id=i)
			t.prod_stock = t.prod_stock - int(request.POST[quantity])
			t.save()
		total_arr.append(request.POST[total])
	sub_total = request.POST["sub_total"]
	if int(t_type_val) == 1:
		bcp = request.POST["bcp"]
		request.session['bcp'] = bcp
	elif int(t_type_val) == 3:
		cp = request.POST["cp"]
		request.session['cp'] = cp
	cgst = request.POST["cgst"]
	sgst = request.POST["sgst"]
	just_total = request.POST["total"]
	grand_total =request.POST["gtotal"]
	request.session['cgst'] = cgst
	request.session['sgst'] = sgst
	request.session['quantity_arr'] = quantity_arr
	request.session['total_arr'] = total_arr
	request.session['sub_total'] = sub_total
	request.session['just_total'] = just_total
	request.session['grand_total'] = grand_total
	paginator = Paginator(sel_prod_objs, 11)
	paginatorq = Paginator(quantity_arr, 11)
	paginatort = Paginator(total_arr, 11)
	page = request.GET.get('page')
	try:
		sel_prod_objs_p = paginator.page(page)
		quantity_arr1 = paginatorq.page(page)
		total_arr1 = paginatort.page(page)
	except PageNotAnInteger:
		sel_prod_objs_p = paginator.page(1)
		quantity_arr1 = paginatorq.page(1)
		total_arr1 = paginatort.page(1)
	except EmptyPage:
		sel_prod_objs_p = paginator.page(paginator.num_pages)
		quantity_arr1 = paginatorq.page(paginatorq.num_pages)
		total_arr1 = paginatort.page(paginatort.num_pages)
	if int(t_type_val) == 1:
		return render(request, 'bill/printp.html',{'sel_prod_objs_p':sel_prod_objs_p,'combo':zip(sel_prod_objs_p,quantity_arr1,total_arr1), 'quantity_arr1':quantity_arr1, 'total_arr1':total_arr1, 'sub_total':sub_total, 'bcp':bcp, 'just_total':just_total, 'grand_total':grand_total, 'cgst':cgst, 'sgst':sgst, 't_type_val':t_type_val, 'billnum':billnum})
	elif int(t_type_val) == 3:
		return render(request, 'bill/printp.html',{'sel_prod_objs_p':sel_prod_objs_p,'combo':zip(sel_prod_objs_p,quantity_arr1,total_arr1), 'quantity_arr1':quantity_arr1, 'total_arr1':total_arr1, 'sub_total':sub_total, 'cp':cp, 'just_total':just_total, 'grand_total':grand_total, 'cgst':cgst, 'sgst':sgst, 't_type_val':t_type_val, 'billnum':billnum})
	else:
		return render(request, 'bill/printp.html',{'sel_prod_objs_p':sel_prod_objs_p,'combo':zip(sel_prod_objs_p,quantity_arr1,total_arr1), 'quantity_arr1':quantity_arr1, 'total_arr1':total_arr1, 'sub_total':sub_total, 'just_total':just_total, 'grand_total':grand_total, 'cgst':cgst, 'sgst':sgst, 't_type_val':t_type_val, 'billnum':billnum})
def printpx(request,page):
	sel_prod_ids = request.session['sel_prod_ids']
	t_type_val = request.session['t_type_val']
	sel_prod_objs = Products.objects.filter(pk__in=sel_prod_ids)
	quantity_arr = request.session['quantity_arr']
	total_arr = request.session['total_arr']
	sub_total = request.session['sub_total']
	billnum = request.session['billnum']
	if int(t_type_val) == 1:
		bcp = request.session['bcp']
	elif int(t_type_val) == 3:
		cp = request.session['cp']
	cgst = request.session['cgst']
	sgst = request.session['sgst']
	just_total = request.session['just_total']
	grand_total = request.session['grand_total']
	paginator = Paginator(sel_prod_objs, 11)
	paginatorq = Paginator(quantity_arr, 11)
	paginatort = Paginator(total_arr, 11)
	page = request.GET.get('page')
	try:
		sel_prod_objs_p = paginator.page(page)
		quantity_arr1 = paginatorq.page(page)
		total_arr1 = paginatort.page(page)
	except PageNotAnInteger:
		sel_prod_objs_p = paginator.page(1)
		quantity_arr1 = paginatorq.page(1)
		total_arr1 = paginatort.page(1)
	except EmptyPage:
		sel_prod_objs_p = paginator.page(paginator.num_pages)
		quantity_arr1 = paginatorq.page(paginatorq.num_pages)
		total_arr1 = paginatort.page(paginatort.num_pages)
	if int(t_type_val) == 1:
		return render(request, 'bill/printp.html',{'sel_prod_objs_p':sel_prod_objs_p,'combo':zip(sel_prod_objs_p,quantity_arr1,total_arr1), 'quantity_arr1':quantity_arr1, 'total_arr1':total_arr1, 'sub_total':sub_total, 'bcp':bcp, 'just_total':just_total, 'grand_total':grand_total, 'cgst':cgst, 'sgst':sgst, 't_type_val':t_type_val, 'billnum':billnum})
	elif int(t_type_val) == 3:
		return render(request, 'bill/printp.html',{'sel_prod_objs_p':sel_prod_objs_p,'combo':zip(sel_prod_objs_p,quantity_arr1,total_arr1), 'quantity_arr1':quantity_arr1, 'total_arr1':total_arr1, 'sub_total':sub_total, 'cp':cp, 'just_total':just_total, 'grand_total':grand_total, 'cgst':cgst, 'sgst':sgst, 't_type_val':t_type_val, 'billnum':billnum})
	else:
		return render(request, 'bill/printp.html',{'sel_prod_objs_p':sel_prod_objs_p,'combo':zip(sel_prod_objs_p,quantity_arr1,total_arr1), 'quantity_arr1':quantity_arr1, 'total_arr1':total_arr1, 'sub_total':sub_total, 'just_total':just_total, 'grand_total':grand_total, 'cgst':cgst, 'sgst':sgst, 't_type_val':t_type_val, 'billnum':billnum})








