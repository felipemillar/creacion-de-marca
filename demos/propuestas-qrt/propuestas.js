/* Interacciones locales de los prototipos. No se envían datos ni se conectan servicios. */
const stages = [
  {name:'Datos con contexto.', description:'Conectar fuentes, alinear tiempos y detectar inconsistencias antes de que lleguen al modelo.', proof:'Origen, calidad y trazabilidad de cada serie.'},
  {name:'Hipótesis a prueba.', description:'Convertir una idea en un experimento reproducible. Comparar escenarios y registrar los límites de cada modelo.', proof:'Experimentos versionados y pruebas fuera de muestra.'},
  {name:'Ejecución con límites.', description:'Traducir señales en órdenes con reglas explícitas. Probar conexiones, respuestas y recuperación ante fallos.', proof:'Reglas de ejecución y controles antes de operar.'},
  {name:'Una operación visible.', description:'Observar posiciones, eventos y estado del sistema. Devolver lo aprendido a la siguiente investigación.', proof:'Registros, alertas y un procedimiento de respuesta.'}
];
document.querySelectorAll('[data-stage]').forEach(button => {
  button.addEventListener('click', () => {
    const index = Number(button.dataset.stage);
    document.querySelectorAll('[data-stage]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    document.querySelectorAll('.system-node').forEach((n,i) => n.classList.toggle('active', i === index));
    document.querySelector('[data-stage-index]').textContent = `0${index+1} / 04`;
    document.querySelector('[data-stage-name]').textContent = stages[index].name;
    document.querySelector('[data-stage-description]').textContent = stages[index].description;
    document.querySelector('[data-stage-proof]').textContent = stages[index].proof;
  });
});
const profiles = [
  {title:'La infraestructura debe acompañar a tu equipo.', text:'Un entorno común para investigar, ejecutar y revisar decisiones. Con responsabilidades claras y conocimiento que permanece en la organización.', items:['Investigación reproducible','Integración con la operación existente','Documentación y transferencia al equipo']},
  {title:'Cada conexión sostiene la experiencia de tus clientes.', text:'Un proyecto de integración que considera plataformas, órdenes y operación. Definimos los componentes y las responsabilidades antes de construir.', items:['Conectividad entre sistemas','Controles y conciliación de órdenes','Monitoreo y procedimientos de soporte']},
  {title:'Tu operativa merece un sistema a su medida.', text:'Una base técnica proporcionada a tus mercados, herramientas y forma de operar. Con visibilidad para comprender qué hace el sistema y cómo intervenir.', items:['Datos y herramientas de investigación','Automatización con reglas explícitas','Seguimiento y capacitación práctica']}
];
const tabs = [...document.querySelectorAll('[data-profile]')];
function selectProfile(button, focus=false){
  const value=profiles[Number(button.dataset.profile)];
  tabs.forEach(t => {t.setAttribute('aria-selected',String(t===button));t.tabIndex=t===button?0:-1;});
  const panel=document.querySelector('[data-profile-panel]');
  panel.setAttribute('aria-labelledby',button.id);
  document.querySelector('[data-profile-title]').textContent=value.title;
  document.querySelector('[data-profile-description]').textContent=value.text;
  document.querySelectorAll('[data-profile-item]').forEach((item,i)=>item.textContent=value.items[i]);
  if(focus)button.focus();
}
tabs.forEach((button,i)=>{
  button.addEventListener('click',()=>selectProfile(button));
  button.addEventListener('keydown',event=>{
    let next;
    if(event.key==='ArrowRight') next=(i+1)%tabs.length;
    if(event.key==='ArrowLeft') next=(i+tabs.length-1)%tabs.length;
    if(event.key==='Home') next=0;
    if(event.key==='End') next=tabs.length-1;
    if(next!==undefined){event.preventDefault();selectProfile(tabs[next],true);}
  });
});

const dialog=document.createElement('dialog');
dialog.setAttribute('aria-labelledby','brief-title');
dialog.innerHTML=`<div class="dialog-inner"><div class="dialog-top"><span class="mono">qrt^ / punto de partida</span><button class="dialog-close" aria-label="Cerrar">×</button></div><h2 id="brief-title">Cuéntanos qué necesitas construir.</h2><p>Prepara un resumen para iniciar la conversación.</p><form class="brief-form"><label>Tu contexto<select name="profile"><option>Institución o equipo de trading</option><option>Broker o plataforma</option><option>Trader independiente</option></select></label><label>El punto de partida<select name="need"><option>Definir una arquitectura</option><option>Construir un laboratorio de investigación</option><option>Llevar una estrategia a operación</option><option>Integrar sistemas existentes</option></select></label><label>¿Qué te gustaría resolver?<textarea name="context" maxlength="1000" placeholder="Por ejemplo: conectar mis herramientas de investigación con la ejecución." required></textarea></label><button class="button" type="submit">Preparar resumen <span aria-hidden="true">↗</span></button><p class="form-note">Muestra interactiva: el resumen se genera en este navegador. No se envían datos.</p></form><section class="brief-result" hidden aria-live="polite"><h3>Tu resumen de proyecto</h3><p class="brief-output"></p><button class="button light" type="button" data-copy>Copiar resumen</button><p class="brief-status" role="status"></p></section></div>`;
document.body.append(dialog);
let previousFocus;
document.querySelectorAll('[data-brief]').forEach(button=>button.addEventListener('click',()=>{previousFocus=button;dialog.showModal();}));
dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('close',()=>previousFocus?.focus());
dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
dialog.querySelector('form').addEventListener('submit',event=>{
  event.preventDefault();
  const data=new FormData(event.target);
  const context=String(data.get('context')).trim();
  if(!context){dialog.querySelector('textarea').setCustomValidity('Describe brevemente lo que necesitas resolver.');dialog.querySelector('textarea').reportValidity();return;}
  const summary=`Proyecto de infraestructura de trading\n\nPerfil: ${data.get('profile')}\nObjetivo: ${data.get('need')}\n\nNecesidad\n${context}\n\nPara la conversación: mercados, herramientas actuales, responsables y alcance esperado.`;
  dialog.querySelector('.brief-output').textContent=summary;
  dialog.querySelector('.brief-result').hidden=false;
  dialog.querySelector('.brief-status').textContent='Resumen preparado. Puedes copiarlo para continuar la conversación.';
  dialog.querySelector('.brief-result').scrollIntoView({block:'nearest',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
});
dialog.querySelector('textarea').addEventListener('input',event=>event.target.setCustomValidity(''));
dialog.querySelector('[data-copy]').addEventListener('click',async()=>{
  const status=dialog.querySelector('.brief-status');
  try{await navigator.clipboard.writeText(dialog.querySelector('.brief-output').textContent);status.textContent='Resumen copiado.';}
  catch{status.textContent='Selecciona el texto del resumen y cópialo manualmente.';}
});
