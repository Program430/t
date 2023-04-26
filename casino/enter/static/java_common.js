function animateWord(word){
    let text = word.dataset.text;
    text.split('').forEach((letter,ind) => {
    let div = document.createElement('div');
    div.innerText = letter;
    setTimeout(()=> word.append(div),ind*200);
  })
}

const word = document.querySelector('.word');
animateWord(word);