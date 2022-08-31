const button = document.getElementById('close_side_menu')
const menu = document.getElementById('aside_menu')
const menu_logo = document.getElementById('aside_logo')
const feature = document.getElementsByClassName('feature')[0]
const shop_container = document.getElementById('shop')
const packages_container = document.getElementById('packages')

const button_add_money = document.getElementById('add_money')
const button_get_menu = document.getElementById('get_menu')

const handle_cart_button = document.getElementById('handle_cart_button')
const cart_popup = document.getElementById('cart-popup')
const button_pay_sale = document.getElementById('pay_sale')

const button_z_sale = document.getElementById('z_smen')
const input = document.getElementById('value_input')
const phone_input = document.getElementById('phone_input')
const add_money_submit_button = document.getElementById('add_money_submit_button')
const mini_cart_wrapper = document.getElementById('mini_cart_wrapper')
const mini_cart_total_price = document.getElementById('mini_cart_total_price')
const check_item_total = document.getElementById('check_item_total')
const chek_generate = document.getElementById('generate_chek')

let check_value = null
let check_value1 = null

setTimeout(() => {
    button.addEventListener("click", handleMenu, {options: 'some_options'})
}, 300)

let cart = []

const addMoneyAsItem = () => {

    let time = new Date()
    let price = input.value
    let phone = phone_input.value

    let paylaod = {
        id: phone,
        phone,
        time,
        name: 'Пополнение ' + phone,
        price,
        count: 1
    }
    if (cart.length===0){
        check_value = Math.random(10,100000) * 1000000000000;
        check_value = Math.ceil(check_value);
        chek_generate.innerHTML = check_value
    }
    cart.push(paylaod)
    showItems()
    console.log('cart after pushing item(money)', cart)
}

const addToCart = (payload) => {
    if (cart.length===0){
        check_value1 = Math.random(10,100000) * 1000000000000;
        check_value1 = Math.ceil(check_value1);
        chek_generate.innerHTML = check_value1
    }
    payload.time = new Date()
    let empty = true
    cart.map((item, index) => {
        if (item.id.toString() === payload.id.toString()) {
            empty = false
            item.count++
        }
    })
    if (empty) {
        cart.push(payload)
    }
    console.log(cart)
    showItems()
    console.log('cart after pushing item(shop)', cart)
}

const removeItem = (id) => {
    cart.map((item, index) => {
        if (item.id.toString() === id.toString()) {
            if (item.count !== 1) {
                item.count--
            } else {
                cart = cart.filter(item => item.id.toString() !== id.toString())
            }
        }
    })
    console.log("cart after removing", cart)
    showItems()
}

const showItems = () => {
    let html = ''
    let total_price = 0
    cart.map((item, key) => {
        let comma_index = item.price.indexOf(',')
        let new_price = null
        if (comma_index !== -1) {
            new_price = item.price.slice(0, comma_index)
        }
        else new_price = item.price
        total_price += (new_price * 1 * item.count)
        html += element = ` <div class="item_lined__wrapper">
        <div class="row">${item.name}</div>
        <div class="row">${item.count}</div>
        <div class="row">${item.price} руб</div>
        <div class="row" onClick="removeItem(${item.id})" style="cursor: pointer">Удалить</div>
    </div>`
    })
    mini_cart_wrapper.innerHTML = html
    mini_cart_total_price.innerHTML = total_price + ' руб'
    check_item_total.innerHTML = total_price + ' руб'
    console.log(total_price)
}

const payAnyWay = () => {
    let currentURL = window.location.href;
    try {
        fetch('addMoneyPhone' + '?cart=' + JSON.stringify(cart) + '&check_value=' + check_value + '&check_value1=' + check_value1, {
            method: "GET",
        })
        console.log('SUCCESS SEND POST CART')
        input.value = ''
        phone_input.value = ''
        cart = []
        chek_generate.innerHTML = ''
        check_value = null
        check_value1 = null
        location.reload()
        showItems()
    } catch {
        console.log('ERROR SEND POST CART')
        console.log(e)
    }
}

const menu_types = {
    closed: '50px',
    opened: '16%'
}

const menu_logo_types = {
    closed: 'hidden',
    opened: 'visible'
}

const feature_types = {
    closed: {
        paddingLeft: '100px'
    },
    opened: {
        paddingLeft: '20%'
    },
}

const cart_popup_types = {
    opened: 'translateY(0px)',
    closed: 'translateY(440px)'
}


add_money_submit_button.addEventListener('click', addMoneyAsItem)
button_get_menu.addEventListener("click", openShop, {type: 'shop'})
button_add_money.addEventListener("click", openPackages, {type: 'packages'})
handle_cart_button.addEventListener("click", handleCart, null)
button_z_sale.addEventListener('click', print_Z, null)

function handleMenu() {
    if (menu.style.width === menu_types.closed) {
        menu.style.width = menu_types.opened
        menu_logo.style.visibility = menu_logo_types.opened
        feature.style.paddingLeft = feature_types.opened.paddingLeft
    } else {
        menu.style.width = menu_types.closed
        menu_logo.style.visibility = menu_logo_types.closed
        feature.style.paddingLeft = feature_types.closed.paddingLeft
    }
}

function openShop() {
    button_get_menu.className = 'cashdesk__tab_btn active_tab'
    button_add_money.className = 'cashdesk__tab_btn'
    shop_container.style.display = 'flex';
    packages_container.style.display = 'none'
}

function openPackages() {
    button_add_money.className = 'cashdesk__tab_btn active_tab'
    button_get_menu.className = 'cashdesk__tab_btn'
    shop_container.style.display = 'none';
    packages_container.style.display = 'flex'
}

function handleCart() {
    if (cart_popup.style.transform === cart_popup_types.closed) {
        cart_popup.style.transform = cart_popup_types.opened
    } else {
        cart_popup.style.transform = cart_popup_types.closed
    }
}

function paySale() {
    button_pay_sale.className = 'buy_button'
    shop_container.style.display = 'none';
    packages_container.style.display = 'flex'
}

function print_Z() {
    button_z_sale.className = "cashdesk__z_btn"
    window.print()
}
