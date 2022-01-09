function getSelectLabel(idname){
  var obj = document.getElementById(idname);
  var idx = obj.selectedIndex;       //インデックス番号を取得
  var val = obj.options[idx].value;  //value値を取得
  var txt  = obj.options[idx].text;  //ラベルを取得
 
  alert('選択したのは「インデックス:' + idx + ' 値:' + val + ' ラベル:' + txt + '」です');
}