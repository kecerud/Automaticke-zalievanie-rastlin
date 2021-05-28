
//Preloader transition
setTimeout(() => {  
    document.querySelector('.fullscreen-video-wrap').remove();
        }, 3.55 * 1000);

//Content timeout        
setTimeout(() => {  
    document.querySelector('main').style.display = 'block';
         }, 2.5 * 1000);

//Change img day-night mode        
const images = {
  day: {
    1: 'static/images/Ikonky/day/auto_on.png',
    2: 'static/images/Ikonky/day/auto_off.png',
    3: 'static/images/Ikonky/day/humid.png',
    4: 'static/images/Ikonky/day/single.png',
    5: 'static/images/Ikonky/day/last_time.png',
    6: 'static/images/Ikonky/day/kvetinac.png'

  },
  night: {
    1: 'static/images/Ikonky/night/auto_on.png',
    2: 'static/images/Ikonky/night/auto_off.png',
    3: 'static/images/Ikonky/night/humid.png',
    4: 'static/images/Ikonky/night/single.png',
    5: 'static/images/Ikonky/night/last_time.png',
    6: 'static/images/Ikonky/night/kvetinac.png'

  }
}
// handleImageChange('day')
function handleImageChange(mode) {
    const currentImages = images[mode];
  
    Object.entries(currentImages).forEach(entry => {
      const [selector, src] = entry;
      document.querySelector(`[data-img="${selector}"]`).src = src;
    });
  }

//Day-Night switch
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.toggle');
    const body = document.body;
  
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('active');
  
      const currentTheme = body.classList.contains('night') ? 'night' : 'day';
      const nextTheme = (currentTheme === 'night' ? 'day' : 'night');
      
      body.classList.replace(currentTheme, nextTheme);
      handleImageChange(nextTheme === 'night' ? 'night' : 'day'); 
    });
    handleImageChange('night');
  });




