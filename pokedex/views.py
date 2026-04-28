from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = [
    "Gengar","Pikachu","Slowpoke","Latios","Latias","Greninja","Charmander","Bulbasaur","Squirtle","Eevee","Snorlax","Dragonite","Lucario","Mewtwo","Mew","Blaziken","Sceptile","Swampert","Garchomp","Tyranitar","Umbreon","Espeon","Sylveon","Infernape","Decidueye","Incineroar"]
    return render(request, 'index.html', {'pokemons': pokemons})


def pokemon_details(request, pokemon):
    return render(request, "details.html", {
        "pokemon": pokemon
    })