import re
from django.db.models import Sum
from django.http      import JsonResponse
from django.views     import View
from daily.models     import State

class DailyView(View):
    def get(self, request):
        state_data = State.objects.prefetch_related('test_set__testresult_set', 'hospitalstatus_set', 'graph_set')
        data_limit = 14
        data = [{
            'id'                  : state.id,
            'name'                : state.name,
            'trend_graph'         : state.graph_set.first().trend_graph.replace('div', 'span'),
            'trend_change'        : re.findall(r'<div>(.+?)\%</div>', state.graph_set.first().trend_graph)[0],
            'trend_color'         : re.findall(r'stroke: (.+?)\;', state.graph_set.first().trend_graph.replace('div', 'span'))[0],
            'new_cases'           : state.test_set.prefetch_related('testresult_set').order_by('-id')[:data_limit]
                .aggregate(Sum('testresult__confirmed_growth'))['testresult__confirmed_growth__sum'],
            'new_cases_per_capita': round(state.test_set.prefetch_related('testresult_set').order_by('-id')[:data_limit]
                .aggregate(Sum('testresult__confirmed_growth'))['testresult__confirmed_growth__sum']/state.populations * 100000),
            'confirmed_cases'     : state.test_set.last().testresult_set.first().confirmed,
            'confirmed_per_capita': state.test_set.last().testresult_set.first().confirmed_per_capita,
            'confirmed_deaths'    : state.hospitalstatus_set.last().death,
            'positive_tests'      : state.test_set.last().testresult_set.first().positive_percent,
            'total_tests'         : state.test_set.last().count,
            'total_hospitalized'  : state.hospitalstatus_set.last().hospitalized,
            'gap_graph'           : state.graph_set.first().gap_graph,
        } for state in state_data.all()]
        return JsonResponse({"result": "success", 'data': data}, status=200)

class SearchDailyView(View):
    def get(self, request, state_id):
        arr_id = state_id.split(',')
        state_data = State.objects.prefetch_related('test_set__testresult_set', 'hospitalstatus_set', 'graph_set').filter(id__in=arr_id)
        graph_limit = 30
        data = [{
            'series': {
                'id': state.id,
                'name': state.name,
                'Deaths': [
                    item.death
                    for item in state.hospitalstatus_set.all()[:graph_limit]],
                'Hospitalizations': [
                    item.hospitalized
                    for item in state.hospitalstatus_set.all()[:graph_limit]],
                'Daily New Cases': [
                    item['testresult__confirmed_growth']
                    for item in state.test_set.prefetch_related('testresult_set').values('testresult__confirmed_growth')[:graph_limit]],
                'Confirmed Cases': [
                    item['testresult__confirmed']
                    for item in state.test_set.prefetch_related('testresult_set').values('testresult__confirmed')[:graph_limit]
                ],
                'Tests': [
                    item.count
                    for item in state.test_set.all()[:graph_limit]
                ],
                '% Positive Tests': [
                    float(item['testresult__positive_percent'])
                    for item in state.test_set.prefetch_related('testresult_set').values('testresult__positive_percent')[:graph_limit]
                ]
            },
        } for state in state_data.all()]
        return JsonResponse({"result": "success", "data": data}, status=200)