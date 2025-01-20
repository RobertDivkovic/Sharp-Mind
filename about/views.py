from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from .models import About
from .forms import CollaborationRequestForm

class AboutPageView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        # Inherit existing context
        context = super().get_context_data(**kwargs)
        
        # Fetch the first About instance or provide a fallback if none exists
        context['about'] = About.objects.first()
        
        # Add the CollaborationRequestForm to the context if the user is authenticated
        if self.request.user.is_authenticated:
            context['collaboration_form'] = CollaborationRequestForm()
        
        return context

class CollaborationRequestView(FormView):
    template_name = "about/collaboration_request.html"
    form_class = CollaborationRequestForm
    success_url = '/about/' # Redirect after successful submission

    def form_valid(self, form):
        """
        Process the valid form submission:
        - Save the data to the database.
        - Add a success message for user feedback.
        """
        form.save()
        messages.success(self.request, "Collaboration request received successfully! We will respond within 12 hours.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle an invalid form submission:
        - Log the errors for debugging.
        - Add an error message for user feedback.
        """
        print("DEBUG: Form is invalid")
        print("DEBUG: Errors -", form.errors)
        messages.error(self.request, "There was an error with your submission. Please try again.")
        return super().form_invalid(form)