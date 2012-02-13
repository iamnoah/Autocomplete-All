import sublime_plugin, sublime

class AutocompleteAll(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        window = sublime.active_window()
        # get results from each tab
        results = [v.extract_completions(prefix) for v in window.views() if v.buffer_id() != view.buffer_id()]
        results = [(item,item) for sublist in results for item in sublist] #flatten
        results = list(set(results)) # make unique
        results.sort() # sort
        return results
