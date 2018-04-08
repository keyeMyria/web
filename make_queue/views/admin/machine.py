from django.views.generic import TemplateView

from make_queue.models import Machine


class MachineControlPanelView(TemplateView):
    template_name = "make_queue/machine_control_panel.html"

    def get_context_data(self):
        return {
            "machine_types": [
                {"name": machine_subclass.literal, "machines": machine_subclass.objects.all()}
                for machine_subclass in Machine.__subclasses__()]
        }
