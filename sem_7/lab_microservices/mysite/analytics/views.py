import numpy as np
from django.shortcuts import render

from django.shortcuts import render
import pandas as pd
from django.views import View
from plotly.offline import plot
import plotly.express as px
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Chart


def index(request):
    # qs = Chart.objects.all()
    # projects_data = [
    #     {
    #         'Project': x.name,
    #         'Start': x.start_date,
    #         'Finish': x.finish_date,
    #         'Responsible': x.responsible.username
    #     } for x in qs
    # ]
    # df = pd.DataFrame(projects_data)
    # fig = px.timeline(
    #     df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    # )
    # fig.update_yaxes(autorange="reversed")
    # gantt_plot = plot(fig, output_type="div")
    np.random.seed(42)

    # Data to be Plotted
    random_x = np.random.randint(1, 101, 100)
    random_y = np.random.randint(1, 101, 100)

    plot = px.Figure(data=[px.Scatter(
        x=random_x,
        y=random_y,
        mode='markers', )
    ])
    context = {'plot_div': plot}
    return render(request, 'analytics/index.html', context)


class AnalyticsView(View):
    def get(self, request, *args, **kwargs):
        # Хардкодированные данные
        analytics_data = {
            "total_visits": 1000,
            "unique_users": 500,
            "average_duration": "5 minutes",
        }

        return render(request, "analytics/analytics_page.html", {"analytics_data": analytics_data})
