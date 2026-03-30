const navBar = document.querySelector('.navbar');


// pc nav
const about = document.getElementById('about__btn')
const skills = document.getElementById('skills__btn')
const projects = document.getElementById('projects__btn')
const contact = document.getElementById('contact__btn')
// === pc nav ===

// mobile nav
const allLi = document.querySelectorAll('li');
const about_nav_btn = document.getElementById('about_nav_btn')
const skills_nav_btn = document.getElementById('skills_nav_btn')
const projects_nav_btn = document.getElementById('projects_nav_btn')
const contact_nav_btn = document.getElementById('contact_nav_btn')
const send = document.getElementById('send__msg');
// mobile nav

// sections
const projects_section = document.querySelector('.projects')
const skills_section = document.querySelector('.skills')
const socials_section = document.querySelector('.socials')
const contact_section = document.querySelector('.contact')
// === sections ===


allLi.forEach((li , index )=> {
    li.addEventListener('click' , (e) => {
        e.preventDefault();
        navBar.querySelector('.active').classList.remove('active');
        li.classList.add('active');

        const indicator = document.querySelector('.indicator');
        indicator.style.transform = `translateX( calc(${index * 75}px) )`
    })
})


about.addEventListener('click' , () => {
    window.scrollTo({
        top: 0 ,
        behavior : 'smooth'
    })
} );
about_nav_btn.addEventListener('click' , () => {
    window.scrollTo({
        top: 0 ,
        behavior : 'smooth'
    })
} );

skills.addEventListener('click' , () => {
    window.scrollTo({
        top: skills_section.offsetTop ,
        behavior : 'smooth'
    })
} )
skills_nav_btn.addEventListener('click' , () => {
    window.scrollTo({
        top: skills_section.offsetTop ,
        behavior : 'smooth'
    })
} )
projects.addEventListener('click' , () => {
    window.scrollTo({
        top: projects_section.offsetTop ,
        behavior : 'smooth'
    })
} )
projects_nav_btn.addEventListener('click' , () => {
    window.scrollTo({
        top: projects_section.offsetTop ,
        behavior : 'smooth'
    })
} )
contact.addEventListener('click' , () => {
    window.scrollTo({
        top: socials_section.offsetTop ,
        behavior : 'smooth'
    })
} )
contact_nav_btn.addEventListener('click' , () => {
    window.scrollTo({
        top: socials_section.offsetTop ,
        behavior : 'smooth'
    })
} )



send.addEventListener('click' , () => {
    window.scrollTo({
        top: contact_section.offsetTop ,
        behavior : 'smooth'
    })
} )




const light_btn = document.querySelectorAll('.dark__mode__btn')
const body = document.querySelector('body');
const link = document.querySelectorAll('.link')
const about__p = document.getElementById('about__p')
const title = document.querySelectorAll('.title')
const moon_icon = document.querySelectorAll('.moon__icon')
const card_tit = document.querySelector('.card__tit')
const footer = document.querySelector('footer')
const hello = document.querySelector('.hello')
const label = document.querySelectorAll('.label')


light_btn.forEach(e => {
    e.addEventListener('click' , () => {
        body.classList.toggle('light__mode');
        link.forEach( el => {
            el.classList.toggle('light__mode__color')
        
        }   )
        about__p.classList.toggle('light__mode__color')
        title.forEach(el => {
            el.classList.toggle('light__mode__color')
        })

        const is_light = body.classList.contains('light__mode')

        moon_icon.forEach( e => {
            e.setAttribute('class' , is_light ? 'ri-sun-line' : 'ri-moon-line')
        })
        card_tit.classList.toggle('dark__mode__color')
        hello.classList.toggle('light__mode__color')
        label.forEach( e => {
            e.classList.toggle('light__mode__color')
        })
    })
}

)


// title script
const originalTitle = document.title ;
const originalIcon = document.querySelector("link[rel = 'icon' ]").href

console.log(originalIcon , originalTitle);

document.addEventListener('visibilitychange' , () => {
    const favicon = document.querySelector('link[ rel = "icon" ]');

    if (document.hidden) {
        document.title = "Comeback to portfolio"
        favicon.href = sadIcon
    }
    else{
        document.title = originalTitle
        favicon.href = originalIcon
    }
} )

// === title script ===

// alert
const alerts = document.querySelectorAll('.alert')

setTimeout( () => {
    alerts.forEach( e => {
        e.classList.add('hide')
    })
} , 5000)
// === alert ===