from kivy.uix.behaviors.compoundselection import CompoundSelectionBehavior
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.app import App


class SelectableBoxLayout(FocusBehavior, CompoundSelectionBehavior, BoxLayout):

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """Based on FocusBehavior that provides automatic keyboard
        access, key presses will be used to select children.
        """
        print(keycode, text, modifiers)
        print(self.orientation)
        if super(SelectableBoxLayout, self).keyboard_on_key_down(
            window, keycode, text, modifiers):
            return True

        if self.orientation == 'horizontal' and keycode[1] in ['up', 'down']:
            self.clear_selection()
            return self.parent.keyboard_on_key_down(window, keycode, text, modifiers)
        if self.orientation == 'vertical' and keycode[1] in ['up', 'down']:
            direction = 'focus_next' if keycode[1] == 'down' else 'focus_previous'

            if self.selected_nodes:
                next_row = self.selected_nodes[0]._get_focus_next(direction)
            else:
                next_row = self.children[-1]
            self.clear_selection()
            self.select_node(next_row)
            if next_row:
                next_row.focus = True
                next = next_row.children[-1]
                if next and not isinstance(next, SelectableBoxLayout):
                    print("moving to {0}".format(next))
                    next.focus = True
                    next_row.clear_selection()
                    next_row.select_node(next)
            return True
        if self.select_with_key_down(window, keycode, text, modifiers):
            return True
        return False

    def keyboard_on_key_up(self, window, keycode):
        """Based on FocusBehavior that provides automatic keyboard
        access, key release will be used to select children.
        """
        if super(SelectableBoxLayout, self).keyboard_on_key_up(window, keycode):
            return True
        if self.orientation == 'horizontal' and keycode[1] in ['up', 'down']:
            return self.parent.keyboard_on_key_up(window, keycode)
        if self.select_with_key_up(window, keycode):
            return True
        return False

    def add_widget(self, widget, index=0):
        """ Override the adding of widgets so we can bind and catch their
        *on_touch_down* events. """
        widget.bind(on_touch_down=self.button_touch_down,
                    on_touch_up=self.button_touch_up)
        return super(SelectableBoxLayout, self).add_widget(widget, index)

    def button_touch_down(self, button, touch):
        """ Use collision detection to select buttons when the touch occurs
        within their area. """
        if button.collide_point(*touch.pos):
            self.select_with_touch(button, touch)

    def button_touch_up(self, button, touch):
        """ Use collision detection to de-select buttons when the touch
        occurs outside their area and *touch_multiselect* is not True. """
        if not (button.collide_point(*touch.pos) or
                self.touch_multiselect):
            self.deselect_node(button)

    def select_node(self, node):
        node.background_color = (1, 0, 0, 1)
        print("select: {}".format(getattr(node, 'text', 'none')))
        return super(SelectableBoxLayout, self).select_node(node)

    def deselect_node(self, node):
        node.background_color = (1, 1, 1, 1)
        print("deselect: {}".format(getattr(node, 'text', 'none')))
        super(SelectableBoxLayout, self).deselect_node(node)

    def on_selected_nodes(self, grid, nodes):
        pass

class TestingappApp(App):
    """Basic kivy app

    Edit testingapp.kv to get started.
    """
    def build(self):
        grid = SelectableBoxLayout(orientation='vertical', touch_multiselect=False,
                              multiselect=False)
        for i in range(0, 6):
            row = SelectableBoxLayout(orientation='horizontal', touch_multiselect=False,
                                       multiselect=False)
            for j in range(0,5):
                b = Button(text="Event A\n TT {}{}".format(i, j))
                row.add_widget(b)
            grid.add_widget(row)
        row.get_focus_next().focus = True
        return grid
TestingappApp().run()