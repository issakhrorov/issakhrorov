let parkings = document.querySelectorAll('.item')
let list = document.getElementById('list')


parkings.forEach(parking => {
    parking.addEventListener('click', event => {
        list.innerHTML = ''

        fetch('/api/parkings')
            .then(res => res.json())
            .then(data => {
                setLots(data, event)
            })
    })
})

function setLots(data, event) {
    data.forEach(parking => {
        if (parking.id == event.target.dataset.id) {
            parking.lots.forEach(lot => {
                let a = document.createElement('a')

                a.setAttribute('class', 'lot')

                if (lot.reserved) a.classList.add('reserved')

                a.textContent = lot.id

                a.addEventListener('click', e => {
                    fetch(`/api/${parking.id}/lots/${lot.id}`, {
                        method: 'POST', 
                        headers: {
                            'Content-Type' : 'application/json'
                        }, 
                        body: JSON.stringify({reserved: true})
                    })
                        .then(res => res.json())
                        .then(data => {
                            if (data.reserved) {
                                e.target.classList.add('reserved')
                            }
                        })
                })


                list.appendChild(a)
            })
        }
    })
}
