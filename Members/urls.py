from django.urls import path, include
from . import views as member_views
from Assessment import views as assessment_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', member_views.login_user, name='login'),
    path('logout', member_views.logout_user, name='logout'),
    path('screening1', assessment_views.screening1, name='screening1'),
    path('screening', assessment_views.screening, name='screening'),
    path('index', assessment_views.home, name='index'),
    path('no_session', assessment_views.no_session, name='no_session'),
    path('pdf', assessment_views.get_pdf, name='pdf'),
    path('result', assessment_views.result, name='result'),
    path('dpia_screening', assessment_views.dpia_screening, name='dpia_screening'),
    path('session_screen', assessment_views.session_screen, name='session_screen'),
    path('risk_summary', assessment_views.risk_summary, name='risk_summary'),
    path('heat_map', assessment_views.heat_map, name='heat_map'),
    path('gdpr_report', assessment_views.gdpr_report, name='gdpr_report'),
    path('pdf_button', assessment_views.pdf_button, name='pdf_button'),
    path('status', assessment_views.status, name='status'),
    path('forget_password', assessment_views.forget_password, name='forget_password'),
    path('risk_summary_details', assessment_views.risk_summary_details, name='risk_summary_details'),
    path('risk_summary', assessment_views.click_risk_summary, name='risk_summary_fun'),
    path('risk_summary_box_1', assessment_views.risk_summary_box_1, name='risk_summary_box_1'),
    path('risk_summary_box_2', assessment_views.risk_summary_box_2, name='risk_summary_box_2'),
    path('risk_summary_box_3', assessment_views.risk_summary_box_3, name='risk_summary_box_3'),
    path('risk_summary_box_4', assessment_views.risk_summary_box_4, name='risk_summary_box_4'),
    path('risk_summary_box_5', assessment_views.risk_summary_box_5, name='risk_summary_box_5'),
    path('risk_summary_box_6', assessment_views.risk_summary_box_6, name='risk_summary_box_6'),
    path('risk_summary_box_7', assessment_views.risk_summary_box_7, name='risk_summary_box_7'),
    path('risk_summary_box_8', assessment_views.risk_summary_box_8, name='risk_summary_box_8'),
    path('change_password/<token>/', assessment_views.change_password, name="change_password")

]