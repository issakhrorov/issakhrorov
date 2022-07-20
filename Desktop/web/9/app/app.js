// core library
let fs = require('fs')
let path = require('path')

//third level library
let express = require('express')
let app = express()

let PORT = 3000

app.set('view engine', 'ejs')

app.use('/static', express.static('public'))

app.get('/', (req, res) => {
    let parkings = JSON.parse(fs.readFileSync('data.json'))
    res.render('index', {parkings: parkings})
})

app.get('/api/parkings', (req, res) => {
    let parkings = JSON.parse(
        fs.readFileSync(path.join(__dirname, 'data.json'))
    )

    res.json(parkings)
})

app.post(`/api/:parking/lots/:lot`, (req, res) => {
    let parkingId = req.params.parking
    let lotId = req.params.lot

    let parkings = JSON.parse(fs.readFileSync(path.join(__dirname, 'data.json')))

    for (let parking of parkings) {
        if (parking.id == parkingId) {
            for (let lot of parking.lots) {
                if (lot.id == lotId) {
                    if (!lot.reserved) {
                        let parkingIdx = parkings.indexOf(parkings)
                        let lotIdx = parking.lots.indexOf(lot)
                        parkings[parkingIdx].lot[lotIdx].reserved = true
                        fs.writeFileSync('data.json', JSON.stringify(parkings))
                        res.json({reserved: true})
                    }
                } else {
                    res.json({reserved: false})
                }
            }
        }
    }
})

app.listen(PORT, err => {
    console.log('App started on port number 3000...')
})
