from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.core.urlresolvers import reverse
from django.core.mail import send_mail


class ContactFormView(FormView):  # WIP

    form_class = ContactForm
    template_name = 'template'  # OVERRIDE!

    success_url = 'success_url' # OVERRIDE!

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context

    def form_valid(self, form):
        subject = form.cleaned_data['topic']

        from_email = form.cleaned_data['email']
        # from_email = '{0} <{0}>'.format(form.cleaned_data['email'])
        # from_email = 'sztosz@gmail.com <sztosz@gmail.com>'
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']

        message = 'IMIĘ I NAZWISKO: {} \nTELEFON {} \n\n{}'.format(name, phone, form.cleaned_data['message'])
        # message = form.cleaned_data['message']

        send_mail(subject, message, from_email, ['m.andreasik@wroc-adwokat.pl'], fail_silently=False)

        return HttpResponseRedirect(self.get_success_url())



class HomePageView(TemplateView):  # DONE

    template_name = 'main_site/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = True
        return context


class AboutPageView(TemplateView):  # DONE

    template_name = 'main_site/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class OfficePageView(TemplateView):  # DONE

    template_name = 'main_site/office.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context



class PricingPageView(TemplateView):  # DONE

    template_name = 'main_site/pricing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class AdvicesPageView(ContactFormView):  # DONE

    template_name = 'main_site/advices.html'
    success_url = 'main_site:advices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class PublicationsPageView(TemplateView):  # DONE

    template_name = 'main_site/publications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class ExtrasPageView(TemplateView):  # WIP

    template_name = 'main_site/extras.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel'] = False
        return context


class ContactPageView(ContactFormView):  # WIP

    template_name = 'main_site/contact.html'
    success_url = 'main_site:contact'
