from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse


class ServicesPageView(TemplateView):  # DONE

    template_name = 'main_site/services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class CriminalPageView(TemplateView):  # DONE

    template_name = 'main_site/services/criminal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class EntrepreneursPageView(TemplateView):  # DONE

    template_name = 'main_site/services/entrepreneurs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class IndividualPageView(TemplateView):  # DONE

    template_name = 'main_site/services/individual.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class PublicPageView(TemplateView):  # DONE

    template_name = 'main_site/services/public.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class FamilyPageView(TemplateView):  # DONE

    template_name = 'main_site/services/family.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class BankruptPageView(TemplateView):  # DONE

    template_name = 'main_site/services/bankrupt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class AdministrationPageView(TemplateView):  # DONE

    template_name = 'main_site/services/administration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class WorkPageView(TemplateView):  # DONE

    template_name = 'main_site/services/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context
