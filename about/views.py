from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from .models import About, CollaborationRequest
from .forms import CollaborationRequestForm


class AboutPageView(TemplateView):
    """
    Displays the About page.

    Template:
        about/about.html

    Features:
        - Displays the first About instance, if available.
        - Provides a collaboration request form for authenticated users.
        - Lists all collaboration requests made by the logged-in user.
    """
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        """
        Prepare the context data for the About page:
        - Fetch the first About instance from the database.
        - Provide the CollaborationRequestForm for authenticated users.
        - Fetch collaboration requests made by the logged-in user.

        Returns:
            dict: A dictionary containing the context data.
        """
        # Inherit existing context
        context = super().get_context_data(**kwargs)

        # Fetch the first About instance or provide a fallback if none exists
        context['about'] = About.objects.first()

        # Add the CollaborationRequestForm and collaboration requests for auth
        if self.request.user.is_authenticated:
            context['collaboration_form'] = CollaborationRequestForm()

            # Fetch all collaboration requests for the logged-in user
            context['collaboration_requests'] = (
                CollaborationRequest.objects.filter(
                    user=self.request.user
                )
            )

        return context


class CollaborationRequestView(CreateView):
    """
    Handles the creation of collaboration requests.

    Template:
        about/collaboration_request.html

    Features:
        - Displays a form for submitting collaboration requests.
        - Associates the request with the logged-in user.
        - Saves the request to the database.
        - Provides user feedback on successful or failed submissions.
    """
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

        Returns:
            HttpResponseRedirect: Redirects to the About page on success.
        """
        # Associate the collaboration request with the logged-in user
        collaboration_request = form.save(commit=False)
        collaboration_request.user = self.request.user
        collaboration_request.save()

        # Provide feedback to the user
        messages.success(self.request, "Collaboration request received!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form submissions:
        - Log errors for debugging.
        - Add an error message for user feedback.

        Returns:
            HttpResponse: Renders the form with error messages.
        """
        # Debugging logs for invalid form
        print("DEBUG: Form is invalid")
        print("DEBUG: Errors -", form.errors)

        # Provide feedback to the user
        messages.error(self.request, "There was an error with your submision.")
        return super().form_invalid(form)


class CollaborationRequestUpdateView(UpdateView):
    """
    Handles the editing of collaboration requests.

    Template:
        about/collaboration_request_form.html

    Features:
        - Allows users to edit their collaboration requests.
        - Provides feedback on successful updates.
    """
    model = CollaborationRequest
    fields = ['name', 'email', 'message']
    template_name = 'about/collaboration_request_form.html'
    success_url = '/about/'

    def form_valid(self, form):
        """
        Handle valid form submissions:
        - Update the collaboration request in the database.
        - Provide feedback to the user.

        Returns:
            HttpResponseRedirect: Redirects to the About page on success.
        """
        messages.success(self.request, "Collaboration request updated!")
        return super().form_valid(form)


class CollaborationRequestDeleteView(DeleteView):
    """
    Handles the deletion of collaboration requests.

    Template:
        about/collaboration_request_confirm_delete.html

    Features:
        - Allows users to delete their collaboration requests.
        - Provides feedback on successful deletions.
    """
    model = CollaborationRequest
    template_name = 'about/collaboration_request_confirm_delete.html'
    success_url = reverse_lazy('about')

    def delete(self, request, *args, **kwargs):
        """
        Handle the deletion of a collaboration request:
        - Remove the request from the database.
        - Provide feedback to the user.

        Returns:
            HttpResponseRedirect: Redirects to the About page on success.
        """
        messages.success(self.request, "Collaboration request deleted!")
        return super().delete(request, *args, **kwargs)
