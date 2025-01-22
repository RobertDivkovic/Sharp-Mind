from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from .models import About, CollaborationRequest
from .forms import CollaborationRequestForm

class AboutPageView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        """
        Prepare the context data for the about page:
        - Include the first About instance.
        - Include the collaboration form for authenticated users.
        - Include collaboration requests for the logged-in user.
        """
        # Inherit existing context
        context = super().get_context_data(**kwargs)
        
        # Fetch the first About instance or provide a fallback if none exists
        context['about'] = About.objects.first()
        
        # Add the CollaborationRequestForm and collaboration requests for authenticated users
        if self.request.user.is_authenticated:
            context['collaboration_form'] = CollaborationRequestForm()
            
            # Fetch all collaboration requests for the logged-in user
            context['collaboration_requests'] = CollaborationRequest.objects.filter(user=self.request.user)
        
        return context

class CollaborationRequestView(CreateView):
    model = CollaborationRequest
    form_class = CollaborationRequestForm
    template_name = 'about/collaboration_request.html'
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        """
        Handle valid form submissions:
        - Associate the request with the logged-in user.
        - Save the data to the database.
        - Add a success message for user feedback.
        """
        # Associate the collaboration request with the logged-in user
        collaboration_request = form.save(commit=False)
        collaboration_request.user = self.request.user
        collaboration_request.save()

        # Provide feedback to the user
        messages.success(self.request, "Collaboration request received successfully! We will respond within 12 hours.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form submissions:
        - Log errors for debugging.
        - Add an error message for user feedback.
        """
        # Debugging logs for invalid form
        print("DEBUG: Form is invalid")
        print("DEBUG: Errors -", form.errors)

        # Provide feedback to the user
        messages.error(self.request, "There was an error with your submission. Please try again.")
        return super().form_invalid(form)

class CollaborationRequestUpdateView(UpdateView):
    model = CollaborationRequest
    fields = ['name', 'email', 'message']
    template_name = 'about/collaboration_request_form.html'
    success_url = '/about/'

    def form_valid(self, form):
        messages.success(self.request, "Collaboration request updated successfully!")
        return super().form_valid(form)

class CollaborationRequestDeleteView(DeleteView):
    model = CollaborationRequest
    template_name = 'about/collaboration_request_confirm_delete.html'
    success_url = reverse_lazy('about')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Collaboration request deleted successfully!")
        return super().delete(request, *args, **kwargs)