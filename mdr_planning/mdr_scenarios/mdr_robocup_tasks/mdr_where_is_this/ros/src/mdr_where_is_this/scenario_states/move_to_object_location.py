from mas_execution_manager.scenario_state_base import ScenarioStateBase

class MoveToObjectLocation(ScenarioStateBase):
    def __init__(self, save_sm_state=False, **kwargs):
        ScenarioStateBase.__init__(self, 'move_to_object_location',
                                   save_sm_state=save_sm_state,
                                   outcomes=['succeeded', 'failed', 'failed_after_retrying'])
        self.sm_id = kwargs.get('sm_id', '')
        self.state_name = kwargs.get('state_name', 'move_to_object_location')
        self.number_of_retries = kwargs.get('number_of_retries', 0)

    def execute(self, userdata):
        if self.save_sm_state:
            self.save_current_state()

        # Check object in the knowledge base.
        # Query location information from ontology.
        location = "living room"
        self.say("Going to " + location)

        return 'succeeded'
