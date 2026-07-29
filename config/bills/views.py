from django.shortcuts import render, redirect
from .forms import ExpenseForm, MemberForm
from .models import Group, Member, Expense


def home(request):
    group = Group.objects.first()
    members = Member.objects.all()
    expenses = Expense.objects.all()

    total_expense = sum(expense.amount for expense in expenses)

    member_count = members.count()

    if member_count > 0:
        share_per_member = total_expense / member_count
    else:
        share_per_member = 0

    settlements = []

    for member in members:
        amount_paid = sum(
            expense.amount
            for expense in expenses
            if expense.paid_by == member
        )

        balance = amount_paid - share_per_member

        settlements.append({
            "member": member,
            "paid": amount_paid,
            "balance": balance,
        })

    context = {
        "group": group,
        "members": members,
        "expenses": expenses,
        "total_expense": total_expense,
        "share_per_member": share_per_member,
        "settlements": settlements,
    }

    return render(request, "bills/home.html", context)


def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ExpenseForm()

    return render(request, "bills/add_expense.html", {"form": form})

def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MemberForm()

    return render(request, "bills/add_member.html", {"form": form})

def edit_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ExpenseForm(instance=expense)

    return render(request, "bills/add_expense.html", {"form": form})

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect("home")