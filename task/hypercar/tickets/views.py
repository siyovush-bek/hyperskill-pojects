from django.views import View
from django.shortcuts import render, redirect

from tickets.database import line_of_cars, get_length, next_ticket


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/welcome.html")


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/menu.html")


class ChangOilView(View):
    def get(self, request, *args, **kwargs):
        number = get_length() + 1
        estimated_time = len(line_of_cars['oil']) * 2
        line_of_cars['oil'].append(number)
        context = {
            'number': number,
            'time': estimated_time
        }
        return render(request, template_name="tickets/oil.html", context=context)


class InflateTires(View):
    def get(self, request, *args, **kwargs):
        number = get_length() + 1
        estimated_time = len(line_of_cars['oil']) * 2 + \
                    len(line_of_cars['tires']) * 5
        line_of_cars['tires'].append(number)
        context = {
            'number': number,
            'time': estimated_time
        }
        return render(request, template_name="tickets/oil.html", context=context)


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        number = get_length() + 1
        estimated_time = len(line_of_cars['oil']) * 2 + \
                    len(line_of_cars['tires']) * 5 + \
                    len(line_of_cars['diagnostic']) * 30
        line_of_cars['diagnostic'].append(number)
        context = {
            'number': number,
            'time': estimated_time
        }
        return render(request, template_name="tickets/oil.html", context=context)


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'oil': len(line_of_cars['oil']),
            'tires': len(line_of_cars['tires']),
            'diagnostic': len(line_of_cars['diagnostic'])
        }
        return render(request, template_name="tickets/processing.html",
                      context=context)

    def post(self, request, *args, **kwargs):
        ticket = next_ticket()
        if ticket:
            line_of_cars['next'] = f'Next ticket #{ticket}'
        else:
            line_of_cars['next'] = 'Waiting for the next client'
        return redirect("/processing")


class NextClientView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'text': line_of_cars['next']
        }
        return render(request, template_name="tickets/next.html",
                      context=context)