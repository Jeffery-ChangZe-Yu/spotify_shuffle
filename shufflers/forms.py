from django import forms


class SongForm(forms.Form):
    numSongs = forms.IntegerField(label="Number of Songs to Queue", required=True)