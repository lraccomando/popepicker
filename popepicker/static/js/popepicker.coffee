@popepicker = {}

@popepicker.init = () =>
    @popepicker.router = new Router()
    Backbone.history.start({pushState:true})


class Router extends Backbone.Router

    routes:
        '': 'home'

    home: () ->
        collection = new PopeCollection()
        view = new HomeView({router:@, collection:collection})
        $('#__content').append(view.render().el)


class HomeView extends Backbone.View

    initialize: (options) ->
        @router = options.router
        @collection = options.collection

    render: () ->
        template = _.template(templates.home_page)
        $(@el).append(template)

        @collection.fetch
            success: (popes) ->
                console.log popes
        return @


class PopeView extends Backbone.View

    initialize: (options) ->
        @router = options.router
        @model = options.model

    render: (options) ->
        template = _.template(templates.pope, {pope:@model})
        $(@el).append(template)
        return @


class Pope extends Backbone.Model

class PopeCollection extends Backbone.Collection
    url: '/data/popes/'
    model: Pope
