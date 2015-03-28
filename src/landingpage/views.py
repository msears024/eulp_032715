from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView


class LandingPageView(TemplateView):
    template_name = 'landingpage/landing.html'
    
    def get_context_data(self, **kwargs):
    	context = super(LandingPageView, self).get_context_data(**kwargs)
    	return context

class PrivacyPolicy(TemplateView):
    template_name = 'landingpage/privacy.html'
    def get_context_data(self, **kwargs):
        context = super(PrivacyPolicy, self).get_context_data(**kwargs)
        return context

class TermsOfUse(TemplateView):
    template_name = 'landingpage/terms.html'
    def get_context_data(self, **kwargs):
        context = super(TermsOfUse, self).get_context_data(**kwargs)
        return context

        