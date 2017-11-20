package components

import (
	"github.com/drekle/go/web/actions"
	"github.com/drekle/go/web/dispatcher"
	"github.com/drekle/go/web/store"
	"github.com/drekle/go/web/store/model"
	"github.com/gopherjs/vecty"
	"github.com/gopherjs/vecty/elem"
	"github.com/gopherjs/vecty/event"
	"github.com/gopherjs/vecty/prop"
)

// FilterButton is a vecty.Component which allows the user to select a filter
// state.
type FilterButton struct {
	vecty.Core

	Label  string            `vecty:"prop"`
	Filter model.FilterState `vecty:"prop"`
}

func (b *FilterButton) onClick(event *vecty.Event) {
	dispatcher.Dispatch(&actions.SetFilter{
		Filter: b.Filter,
	})
}

// Render implements the vecty.Component interface.
func (b *FilterButton) Render() *vecty.HTML {
	return elem.ListItem(
		elem.Anchor(
			vecty.Markup(
				vecty.MarkupIf(store.Filter == b.Filter, prop.Class("selected")),
				prop.Href("#"),
				event.Click(b.onClick).PreventDefault(),
			),

			vecty.Text(b.Label),
		),
	)
}
