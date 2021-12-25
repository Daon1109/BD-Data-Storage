function nightDay(self) {
  var lazy = document.querySelectorAll('#input_text');
  var i;
  if(self.value==='NightMode') {
    document.querySelector('body').style.backgroundColor='black';
    document.querySelector('body').style.color='lightgray';
    for (i = 0; i < lazy.length; i++) {
      lazy[i].style.color='lightgray';
      lazy[i].style.backgroundColor='black';
    }
    self.value=' DayMode ';
    self.className = 'daymode';
  }
  else {
    document.querySelector('body').style.backgroundColor='white';
    document.querySelector('body').style.color='black';
    for (i = 0; i < lazy.length; i++) {
      lazy[i].style.color='black';
      lazy[i].style.backgroundColor='white';
    }
    self.value='NightMode';
    self.className = 'nightmode';
  }
}
