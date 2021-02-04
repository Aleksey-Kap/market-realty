
(function() {
  let caseSumsToSep = document.querySelectorAll('span.price');
  caseSumsToSep.forEach(makeNumSep);
  function makeNumSep(item, index) {
    let workValue = item.innerHTML;
    item.innerHTML = parseFloat(workValue).toLocaleString('ru-RU',).replace(',', '.');
  }
}) ();
