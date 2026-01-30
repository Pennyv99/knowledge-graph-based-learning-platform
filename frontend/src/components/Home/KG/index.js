// const arr = [1,2,3,3];
// const uniqueArr = [...new Set(arr)];
// console.log(uniqueArr);
// function throttle(fn,delay){
//   let lastCall = 0;
//   return function(...args){
//     const now  = Date.now();
//     if (now-lastCall >= delay){
//       lastCall = now;
//       fn.apply(this,args);
//     }
//   }
// }
// const onScroll = throttle(()=>{
//   console.log("触发滚动",Date.now());
// },1000);
// window.addEventListener("scroll",onScroll);
//
// function fn() {
//   return console.log(this.a)
// }
// let obj = {
//   a:2,
//   fn: function fn() {
//   return console.log(this.a)
// }
// }
// function Person() {
//   this.age = 0
//   function () {function () {
//     console.log(this.age)     // => undefined
//   }}
// }
// var p = new Person()
// var fullName = 'language';
//
// var obj = {
//   fullName: 'javascript',
//   prop: {
//     getFullName: function () {
//       return this.fullName;
//     }
//   }
// };
//
// console.log(obj.prop.getFullName());
// var num = 10
// var obj = {num: 20}
// obj.fn = (function (num) {
//   this.num = num * 3
//   num++
//   return function (n) {
//     this.num += n
//     num++
//     console.log(num)
//   }
// })(obj.num)
// var fn = obj.fn
// fn(5)
// obj.fn(10)
// console.log(num, obj.num);
// function count(){
//   let i = 0;
//   return function(){
//     i++;
//     console.log(`函数被调用了${i}次`)
//   }
// }
// const btn = document.getElementById('btn');
// const fn = count();
// btn.addEventListener('click',fn);
// const sayHi = () => console.log("Hi!");
// function once(args){
//   let i = 0;
//   return ()=>{
//     if(i == 0){
//       args();
//     }
//   i++;}
// }
// const onceSayHi = once(sayHi);
//
// onceSayHi(); // 输出：Hi!
// onceSayHi(); // 不输出 ✅
function deepClone(obj,map = new WeakMap()){
  if(typeof obj !== 'object' || obj === null){
    return obj;
  }
  if(map.has(obj)){
    return map.get(obj);
  }
  let clone = Array.isArray(obj)? []:{};
  map.set(obj,clone);
  for(let key in obj){
    if(obj.hasOwnProperty(key)){
    clone[key] = deepClone(obj[key],map);
    }
  }
  return clone;


}

// function deepClone(obj,map = new WeakMap()){
//   if(typeof(obj) != 'object' || obj === null){
//     return obj;
//   }
//   if(map.has(obj)){
//     return map.get(obj);
//   }
//   let clone = Array.isArray(obj)? []:{};
//   map.set(obj,clone);
//   for(const key in obj){
//     if(obj.hasOwnProperty(key)){
//       clone[key] = deepClone(obj[key],map);
//     }
//   }
//   return clone;
// }
// const obj = { a: 1, b: { c: 2 }, d: [3, 4] };
// let copyObj = deepClone(obj);
// console.log(copyObj);
// // 实现 deepClone(obj) → 返回一个值完全相同但地址不同的新对象
// class EventEmitter{
//   constructor() {
//     this.events = {};
//   }
//   on(event,fn){
//     if(!this.events[event]){
//       this.events[event] = [];
//     }
//     this.events[event].push(fn);
//   }
//   emit(event,...args){
//     if(!this.events[event]) return;
//     for(let e of this.events[event]){
//       e(...args);
//     }
//   }
//   off(event,fn){
//     if(this.events[event]){
//       this.events[event] = this.events[event].filter(efn => efn !== fn);
//     }
//   }
// }
// const emitter = new EventEmitter();
//
// function hello(data) {
//   console.log("Hello", data);
// }
//
// emitter.on('greet', hello);
// emitter.emit('greet', 'Penny'); // 输出 Hello Penny
// emitter.off('greet', hello);
// emitter.emit('greet', 'Penny'); // ❌ 不输出
const arr = ['a', 'b', 'a', 'c', 'b', 'a'];

const freqMap = arr.reduce((acc, cur) => {
  acc[cur] = (acc[cur] || 0) + 1;
  return acc;
}, {});