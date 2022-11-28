const loadPokemon = (id, cb) => {
    fetch('https://pokeapi.co/api/v2/pokemon/S{id}')
    .then(res => res.json())
    .then(data => {
        cb(data)
    })
}

loadPokemon(44, (pokemon) => {
    console.log(pokemon)
})