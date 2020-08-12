import json
import time
import requests
from django.db.models.functions import Now
from django.http                import JsonResponse
from bs4                        import BeautifulSoup
from selenium                   import webdriver
from django.views               import View
from daily.models               import (
    State,
    Test,
    TestResult,
    HospitalStatus,
    Graph
)
from hospital.models            import (
    Bed,
    Icu
)
from mobility.models import Mobility, Place
from total.models import Total

class TotalCrawlingView(View):
    def get(self, request):
        driver = webdriver.Chrome(r'C:\develop\server_project\esop_crawling\chromedriver.exe')
        driver.get('https://datausa.io/coronavirus')
        time.sleep(6)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        item_list = soup.find('div', {'class': 'profile-stats'}).find_all('div', {'class': 'Stat'})

        for item in item_list:
            print(item.find('div', {'class': 'stat-title'}).text)
            print(item.find('div', {'class': 'stat-value'}).text)
            print(item.find('div', {'class': 'stat-subtitle'}).text)
            Total(
                title     =item.find('div', {'class': 'stat-title'}).text,
                value     =item.find('div', {'class': 'stat-value'}).text,
                sub_title =item.find('div', {'class': 'stat-subtitle'}).text,
                is_deleted=False,
                created_at=Now(),
                updated_at=Now()
            ).save()
        return JsonResponse({'result': "total_crawling_success"}, status=200)

class DailyCrawlingView(View):
    def get(self, request):
        result = json.loads(requests.get("https://datausa.io/api/covid19/states").text)
        filtered_list = list(
            filter(
                lambda item: ('2020/07/' in item['Date'] or '2020/08' in item['Date'])
                             and item['Geography'] != 'American Samoa', result['data']))

        for i in filtered_list:
            if State.objects.filter(name=i['Geography']).exists():
                state_id = State.objects.get(name=i['Geography']).id
            else:
                state = State(
                    name       =i['Geography'],
                    populations=i['Population'],
                    is_deleted =False,
                    created_at =Now(),
                    updated_at =Now()
                )

                state.save()

                state_id = state.id

            test = Test(
                state_id  =state_id,
                count     =i['Tests'],
                is_deleted=False,
                created_at=Now(),
                updated_at=Now()
            )

            test.save()

            test_result = TestResult(
                test_id             =test.id,
                confirmed_growth    =i['ConfirmedGrowth'],
                confirmed           =i['Confirmed'],
                confirmed_per_capita=i['ConfirmedPC'],
                positive_percent    =i['PositivePct'],
                is_deleted          =False,
                created_at          =Now(),
                updated_at          =Now()
            )

            test_result.save()

            hospital_status = HospitalStatus(
                state_id    =state_id,
                hospitalized=i['Hospitalized'],
                death       =i['Deaths'],
                is_deleted  =False,
                created_at  =Now(),
                updated_at  =Now()
            )

            hospital_status.save()

        return JsonResponse({'result': "daily_crawling_success", 'data': filtered_list}, status=200)

class ElementCrawlingView(View):
    def get(self, request):
        driver = webdriver.Chrome(r'C:\develop\server_project\esop_crawling\chromedriver.exe')
        driver.get('https://datausa.io/coronavirus')
        time.sleep(6)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        row_list = soup.find('table', {'class': 'state-table'}).find_all('tr')

        for item in row_list:
            state_name  = item.find('td', {'class': 'Geography'})
            trend_graph = item.find('td', {'class': 'Trend'})
            gap_graph   = item.find('td', {'class': 'Curve'})

            if state_name is not None:
                state_id = State.objects.get(name=state_name.text).id
                Graph(
                    state_id   =state_id,
                    trend_graph=str(trend_graph.find('svg')) + "<div>" + trend_graph.text + "</div>",
                    gap_graph  =str(gap_graph.find('svg')),
                    is_deleted =False,
                    created_at =Now(),
                    updated_at =Now()
                ).save()

        return JsonResponse({'result': "element_crawling_success"}, status=200)

class MobilityCrawlingView(View):
    def get(self, request):
        place_arr = ['Workplaces', 'Grocery and Pharmacy', 'Parks', 'Residential', 'Retail and Recreation', 'Transit Stations']
        for place in place_arr:
            Place.objects.create(name=place)

        result = json.loads(requests.get("https://datausa.io/api/covid19/mobility/states").text)

        for i in result['data']:
            if "2020/07" in i['Date']:
                print(i['Date'])
                print(i['Geography'])
                print(i['Type'])
                print(i['Percent Change from Baseline'])
                Mobility.objects.create(state     =State.objects.get(name=i['Geography']),
                                        place     =Place.objects.get(name=i['Type']),
                                        visit_rate=i['Percent Change from Baseline'])
        return JsonResponse({'result': "mobility_crawling_success"}, status=200)

class HospitalCrawlingView(View):
    def get(self, request):
        result = json.loads(requests.get("https://datausa.io/api/covid19/old/state").text)
        bed_list = result['beds']
        icu_list = result['icu']

        print(len(bed_list))
        print(len(icu_list))

        for i in bed_list:
            state_id = State.objects.get(name=i['Geography']).id
            Bed(
                state_id         =state_id,
                beds_per_thousand=i['Total'],
                is_deleted       =False,
                created_at       =Now(),
                updated_at       =Now()
            ).save()

        for a in icu_list:
            state_id = State.objects.get(name=a['Geography']).id
            Icu(
                state_id        =state_id,
                total           =a['Total'],
                total_per_capita=a['TotalPC'],
                is_deleted      =False,
                created_at      =Now(),
                updated_at      =Now()
            ).save()

        return JsonResponse({'result': "hospital_crawling_success", 'beds': bed_list, 'icu': icu_list}, status=200)
