<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMR SUITE | BAJO RELIEVE</title>
    
    <!-- Fuentes y Librerías -->
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>

    <style>
        /* === DISEÑO COMPILADO (MODO OFFLINE CONTRA BLOQUEOS DE NAVEGADOR) === */
        :root { --brand-dark: #0f172a; --brand-accent: #6366f1; --bg-canvas: #f1f5f9; }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Manrope', sans-serif; background-color: var(--bg-canvas); color: #1e293b; display: flex; flex-direction: column; height: 100vh; overflow: hidden; font-size: 13.5px; }
        
        @media (min-width: 1024px) { 
            body { flex-direction: row; } 
            .lg\:w-3\/12 { width: 25%; }
            .lg\:w-9\/12 { width: 75%; }
        }

        .panel-left { width: 100%; background-color: white; height: 100%; display: flex; flex-direction: column; border-right: 1px solid #e2e8f0; box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1); z-index: 30; overflow-y: auto; padding: 1.25rem; }
        @media (min-width: 1024px) { .panel-left { width: 25%; } }
        
        .panel-right { width: 100%; height: 100%; display: flex; flex-direction: column; background-color: #e2e8f0; overflow: auto; padding: 1.5rem; align-items: center; }
        @media (min-width: 1024px) { .panel-right { width: 75%; } }

        .input-exec { width: 100%; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 5px; font-size: 13px; font-weight: 600; background: white; transition: all 0.2s; margin-bottom: 5px; font-family: inherit;}
        .input-exec:focus { outline: none; border-color: var(--brand-accent); box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1); }
        .label-exec { display: block; font-size: 11px; text-transform: uppercase; font-weight: 800; color: #475569; margin-bottom: 3px; }
        .txt-red { color: #dc2626 !important; font-weight: 800 !important; }
        #sheetLogoBox { height: 110px; width: auto; max-width: 300px; display: flex; align-items: center; justify-content: flex-start; }
        #sheetLogoBox img { height: 75px; width: auto; object-fit: contain; }
        .btn-main { background-color: #0f172a; color: white; padding: 10px; border-radius: 5px; font-weight: 700; text-transform: uppercase; font-size: 11px; width: 100%; transition: all 0.2s; cursor: pointer; text-align: center; border: none; font-family: inherit;}
        .btn-main:hover { background-color: #4f46e5; }
        .separator-row { background-color: #f8fafc !important; color: #475569; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; text-align: center; border-top: 2px solid #e2e8f0; border-bottom: 2px solid #e2e8f0; }
        .acc-cell { display: flex; justify-content: center; align-items: center; gap: 10px; height: 100%; border: none !important; }
        .btn-icon { cursor: pointer; transition: transform 0.1s; border: none; background: transparent; font-size: 14px; padding: 0;}
        .btn-icon:hover { transform: scale(1.2); }
        
        .worker-item { display: flex; justify-content: space-between; align-items: center; padding: 4px 8px; border-bottom: 1px solid #e2e8f0; font-size: 11px; }
        .worker-item:last-child { border-bottom: none; }
        .worker-item:hover { background-color: #f8fafc; }
        ::-webkit-scrollbar { width: 6px; } ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
        
        .btn-header { padding: 0.5rem 1rem; border-radius: 0.25rem; font-size: 11px; font-weight: 700; text-transform: uppercase; cursor: pointer; border: none; transition: all 0.2s; display: flex; align-items: center; gap: 0.25rem; }
        .btn-header-white { background-color: white; border: 1px solid #cbd5e1; color: #334155; }
        .btn-header-white:hover { background-color: #f8fafc; }
        .btn-header-green { background-color: #059669; color: white; }
        .btn-header-green:hover { background-color: #047857; }
        .btn-header-red { background-color: #e11d48; color: white; }
        .btn-header-red:hover { background-color: #be123c; }
        .btn-header-blue { background-color: #2563eb; color: white; }
        .btn-header-blue:hover { background-color: #1d4ed8; }

        @media print { .no-print { display: none !important; } }
    </style>
</head>
<body>

    <!-- === PANEL IZQUIERDO (Control) === -->
    <div class="panel-left">
        <div class="p-4 bg-slate-900 text-white rounded shadow-lg text-center" style="flex-shrink: 0; margin-bottom: 1.25rem;">
            <h1 class="font-bold text-sm text-amber-400 uppercase" style="letter-spacing: 0.1em;">AMR SUITE V7.1.0</h1>
            <span class="text-xs text-slate-400">Respaldo Local + Netlify</span>
        </div>

        <!-- 1. IDENTIFICACIÓN -->
        <section class="mb-4">
            <span class="label-exec text-indigo-700 italic" style="text-decoration: underline;">1. Identificación</span>
            <input type="text" id="companyName" class="input-exec" placeholder="NOMBRE EMPRESA" oninput="saveConfig()">
            <input type="text" id="companyNIT" class="input-exec" placeholder="NIT" oninput="saveConfig()">
            <input type="text" id="preparedBy" class="input-exec" style="border-left: 4px solid #fbbf24;" placeholder="ELABORADO POR (Obligatorio)..." oninput="saveConfig()">
            
             <label class="block mt-2 cursor-pointer" style="margin-top: 0.5rem;">
                <span class="text-xs text-indigo-600 font-bold" style="text-decoration: underline;">📂 Subir logo</span>
                <input type="file" accept="image/*" class="hidden" onchange="handleLogoUpload(this)">
            </label>
        </section>

        <!-- 2. REGISTRO DE NOVEDAD -->
        <section class="border-t border-slate-200 pt-3 mb-4">
            <span class="label-exec text-indigo-700 font-black italic underline">2. Registro de Novedad</span>
            
            <div style="display: flex; gap: 0.25rem; margin-bottom: 0.5rem;">
                <input type="month" id="reportMonth" class="input-exec" onchange="updatePeriod()">
                <select id="qSelect" class="input-exec" onchange="updatePeriod()"><option value="1">1ª Quincena</option><option value="2">2ª Quincena</option></select>
            </div>
            
            <select id="employeeSelect" class="input-exec" onchange="showEmpData()">
                <option value="">Seleccionar Trabajador...</option>
            </select>
            
            <div id="empDetails" class="p-2 bg-yellow-50 rounded border border-yellow-200 hidden text-xs font-bold mb-2">
                <span id="detDoc"></span> | <span id="detSal" class="text-indigo-600"></span>
            </div>
            
            <label class="label-exec mt-2">Tipo de Novedad</label>
            <select id="novType" class="input-exec" onchange="configFields()">
                <option value="">Seleccione Novedad...</option>
                <option value="Aumento Salarial">Aumento Salarial</option>
                <option value="Comisión">Comisión</option>
                <option value="Horas extras - Recargos">Horas extras - Recargos</option>
                <option value="Incapacidad por Accidente Laboral ARL">Incapacidad por Accidente Laboral ARL</option>
                <option value="Incapacidad por enfermedad General EPS">Incapacidad por enfermedad General EPS</option>
                <option value="Ingreso Laboral">Ingreso Laboral</option>
                <option value="Licencia Maternidad">Licencia Maternidad</option>
                <option value="Licencia de Paternidad">Licencia de Paternidad</option>
                <option value="Permiso NO Remunerado">Permiso NO Remunerado</option>
                <option value="Permiso Remunerado">Permiso Remunerado</option>
                <option value="Retiro Laboral">Retiro Laboral</option>
                <option value="Vacaciones">Vacaciones</option>
            </select>

            <input type="text" id="incapPercent" class="input-exec" placeholder="% INCAP">
            <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.25rem; margin-bottom: 0.25rem;">
                <div><label class="label-exec">Inicio</label><input type="date" id="dateStart" class="input-exec" onchange="calcDays()"></div>
                <div><label class="label-exec">Fin</label><input type="date" id="dateEnd" class="input-exec" onchange="calcDays()"></div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.25rem; margin-bottom: 0.25rem;">
                <div><label class="label-exec">Días</label><input type="number" id="dDays" class="input-exec text-center" placeholder="Días" oninput="calcVal()"></div>
                <div><label class="label-exec">Valor</label><input type="text" id="dVal" class="input-exec text-right" placeholder="Valor $"></div>
            </div>
            <textarea id="dObs" class="input-exec" style="height: 4rem;" placeholder="Observaciones..."></textarea>
            
            <input type="hidden" id="rawSalary" value="0">
            <input type="hidden" id="dStart"><input type="hidden" id="dEnd">

            <button onclick="addRec()" class="btn-main mt-1" style="background-color: #0f172a;">AGREGAR NOVEDAD</button>
        </section>

        <!-- 3. HISTORIAL DE REPORTES -->
        <section class="bg-indigo-50 p-3 rounded border border-indigo-100 mb-4">
            <span class="label-exec text-indigo-800 font-black italic underline">3. Historial de Reportes</span>
            <div id="historyList" class="mt-2" style="max-height: 10rem; overflow-y: auto; display: flex; flex-direction: column; gap: 0.5rem;"></div>
        </section>

        <!-- 4. GESTIÓN DE PERSONAL -->
        <section class="bg-slate-100 p-3 rounded border border-slate-300 mb-8">
            <span class="label-exec text-slate-800 font-black italic underline">4. Gestión de Personal</span>
            <div class="mt-2" style="display: flex; flex-direction: column; gap: 0.5rem;">
                <input type="text" id="newEmpName" class="input-exec" placeholder="Nombre Completo">
                <div style="display: flex; gap: 0.25rem;">
                    <select id="newEmpType" class="input-exec" style="width: 33%;">
                        <option value="CC">CC</option><option value="CE">CE</option>
                        <option value="PPT">PPT</option><option value="PEP">PEP</option><option value="TI">TI</option>
                    </select>
                    <input type="text" id="newEmpDoc" class="input-exec" style="width: 67%;" placeholder="Número">
                </div>
                <input type="number" id="newEmpSal" class="input-exec" placeholder="Salario Base">
                <button onclick="addEmployee()" class="btn-main" style="background-color: #4f46e5;">Guardar Trabajador</button>
            </div>
            
            <div class="mt-3 border-t border-slate-300 pt-2">
                <label class="label-exec text-slate-500">Lista Actual (Click 🗑️ para borrar)</label>
                <div id="workerListContainer" class="bg-white border border-slate-200 rounded" style="max-height: 6rem; overflow-y: auto;"></div>
            </div>
        </section>
    </div>

    <!-- === VISTA PREVIA (Derecha) === -->
    <div class="panel-right">
        
        <!-- TOOLBAR CON BACKUP -->
        <div style="width: 100%; max-width: 72rem; display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;" class="no-print">
            <!-- BOTONES DE RESPALDO -->
            <div style="display: flex; gap: 0.5rem;">
                <button onclick="exportBackup()" class="btn-header btn-header-blue shadow-sm" title="Descarga una copia de toda tu información">💾 Guardar Copia de Seguridad</button>
                <label class="btn-header btn-header-white shadow-sm" style="margin: 0;" title="Sube tu copia para restaurar">
                    📂 Restaurar Copia
                    <input type="file" accept=".json" class="hidden" onchange="importBackup(event)">
                </label>
            </div>

            <div style="display: flex; gap: 0.5rem;">
                <button onclick="clearForNew()" class="btn-header btn-header-white shadow-sm">✨ Nueva Hoja</button>
                <button onclick="downloadExcel()" class="btn-header btn-header-green shadow-sm">📊 Excel</button>
                <button onclick="generatePDF()" class="btn-header btn-header-red shadow-md">📄 PDF</button>
            </div>
        </div>

        <div id="captureArea" class="bg-white w-full max-w-6xl shadow-2xl border min-h-850 p-12 flex flex-col" style="border-color: #e2e8f0; min-height: 850px;">
            <div class="flex justify-between items-start mb-8 border-b-2 border-slate-900 pb-4">
                <div id="sheetLogoBox"></div>
                <div class="text-right">
                    <h2 class="text-xl font-bold text-indigo-600 uppercase">NOVEDADES DE NÓMINA - SEGURIDAD SOCIAL</h2>
                    <div class="flex justify-end gap-5 text-sm font-bold text-slate-700 mt-2 uppercase">
                        <span id="dispQ1">---</span><span id="dispPeriod">---</span>
                    </div>
                </div>
            </div>

            <div class="bg-slate-50 px-8 py-4 border-b border-slate-200 flex flex-col md:flex-row gap-8 items-center md:items-start mb-6">
                <div class="flex-1">
                    <span class="block text-xs font-bold text-slate-400 uppercase mb-1" style="letter-spacing: 0.1em;">Empresa / Razón Social</span>
                    <h2 class="text-lg font-bold text-slate-800" id="sheetCompanyTitle" style="line-height: 1;">---</h2>
                </div>
                <div class="text-right">
                    <span class="block text-xs font-bold text-slate-400 uppercase mb-1" style="letter-spacing: 0.1em;">NIT / Identificación</span>
                    <p class="text-xl font-mono font-bold text-slate-600" id="sheetCompanyNIT" style="line-height: 1;">---</p>
                </div>
            </div>

            <div class="flex-1 overflow-x-auto">
                <table style="width: 100%; font-size: 11px; text-align: left; border-collapse: collapse;" id="mainTable">
                    <thead>
                        <tr style="background-color: #0f172a; color: white; text-transform: uppercase; font-size: 10px;">
                            <th style="padding: 0.75rem; border: 1px solid #334155; width: 12rem;">TRABAJADOR</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; width: 6rem;">DOC</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155;">NOVEDAD</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; text-align: center; width: 4rem;">% INCAP</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; text-align: center; width: 5rem;">INICIO</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; text-align: center; width: 5rem;">FIN</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; text-align: center; width: 3rem;">DÍAS</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; text-align: right; width: 6rem;">VALOR</th>
                            <th style="padding: 0.75rem; border: 1px solid #334155; width: 20%;">OBSERVACIONES</th>
                            <th class="no-print" style="padding: 0.75rem; border: 1px solid #334155; text-align: center; width: 5rem;">ACC</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody" style="border-bottom: 1px solid #cbd5e1;"></tbody>
                </table>
            </div>
            
            <div class="mt-8 pt-4 border-t border-slate-200 flex justify-between items-center text-xs font-bold uppercase text-slate-400">
                <div>Elaborado por: <span id="dispSign" class="text-slate-900 ml-2 italic text-sm">---</span></div>
                <div>AMR Consultoría © 2026 - Control Documental</div>
            </div>
        </div>
    </div>

    <!-- LÓGICA -->
    <script>
        // --- 1. BASE DE DATOS EXACTA REQUERIDA (Los 7 Trabajadores) ---
        const defaultEmployees = [
            { id: 1, name: "Cristian David Ramirez Estrada", doc: "C.C. 1000747333", sal: 1750905 },
            { id: 2, name: "David Coronado Cuadrado", doc: "C.C. 1015069712", sal: 1950905 },
            { id: 3, name: "Jhon Alejandro Muñoz Legarda", doc: "C.C. 1040739221", sal: 2100000 },
            { id: 4, name: "John Fredy Sanchez Zapata", doc: "C.C. 98659334", sal: 1750905 },
            { id: 5, name: "Luis Rivas", doc: "P.P.T. 5052949", sal: 1750905 },
            { id: 6, name: "Teófilo Ariza Gamboa", doc: "C.C. 79598483", sal: 2250905 },
            { id: 7, name: "Juan Felipe Ramírez Meneses", doc: "C.C. 3414736", sal: 1750905 }
        ];

        let employees = JSON.parse(localStorage.getItem('AMR_EMPLOYEES'));
        if (!employees || employees.length === 0) {
            employees = defaultEmployees;
            localStorage.setItem('AMR_EMPLOYEES', JSON.stringify(employees));
        }

        let records = [];
        const COP = new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 });

        // --- SISTEMA DE RESPALDO (JSON Export/Import) ---
        function exportBackup() {
            try {
                let backupData = {};
                for (let i = 0; i < localStorage.length; i++) {
                    const key = localStorage.key(i);
                    if (key.startsWith('AMR_') || key.startsWith('amr_')) {
                        backupData[key] = localStorage.getItem(key);
                    }
                }
                const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(backupData));
                const downloadNode = document.createElement('a');
                downloadNode.setAttribute("href", dataStr);
                const fecha = new Date().toISOString().split('T')[0];
                downloadNode.setAttribute("download", `Respaldo_Nomina_AMR_${fecha}.json`);
                document.body.appendChild(downloadNode);
                downloadNode.click();
                downloadNode.remove();
                alert("✅ Copia de seguridad descargada. Guárdala en un lugar seguro.");
            } catch (err) { alert("Error al guardar copia: " + err.message); }
        }

        function importBackup(event) {
            const file = event.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    const data = JSON.parse(e.target.result);
                    if(confirm("⚠️ ¿Estás seguro de restaurar esta copia? Reemplazará la información actual.")) {
                        for (const key in data) { localStorage.setItem(key, data[key]); }
                        alert("✅ Copia restaurada exitosamente. La página se recargará.");
                        location.reload();
                    }
                } catch(err) { alert("❌ Error: El archivo no es un respaldo válido."); }
            };
            reader.readAsText(file);
        }

        // --- UTILS ---
        const clean = (val) => (val && val.toString().trim() !== "" && val !== "0") ? val : "No aplica";
        const renderVal = (v) => v === 'No aplica' ? '<span style="color:#dc2626; font-weight:800">No aplica</span>' : v;
        const fmtCur = (v) => {
             if (!v || v === "No aplica") return v;
             const num = parseFloat(v.toString().replace(/[^0-9]/g, ''));
             if (isNaN(num)) return v;
             return "$ " + num.toLocaleString('es-CO');
        };
        const toTitleCase = (str) => str.toLowerCase().split(' ').map(w => w.charAt(0).toUpperCase() + w.substring(1)).join(' ');

        // --- INIT ---
        document.addEventListener('DOMContentLoaded', () => {
            const mIn = document.getElementById('reportMonth');
            if(mIn) mIn.value = new Date().toISOString().slice(0, 7);
            
            document.getElementById('dateStart').addEventListener('change', function() { document.getElementById('dStart').value = this.value; calcDays(); });
            document.getElementById('dateEnd').addEventListener('change', function() { document.getElementById('dEnd').value = this.value; calcDays(); });
            
            loadSettings();
            refreshEmployeeUI();
            updatePeriod(); 
            refreshHistoryList();
        });

        // --- GESTIÓN DE PERSONAL ---
        function addEmployee() {
            const rawName = document.getElementById('newEmpName').value;
            const type = document.getElementById('newEmpType').value;
            const docNum = document.getElementById('newEmpDoc').value;
            const sal = document.getElementById('newEmpSal').value;
            
            if(!rawName || !docNum) return alert("⚠️ Nombre y Número de documento son obligatorios.");
            
            employees.push({ id: Date.now(), name: toTitleCase(rawName), doc: `${type} ${docNum}`, sal: sal || 0 });
            localStorage.setItem('AMR_EMPLOYEES', JSON.stringify(employees));
            ['newEmpName','newEmpDoc','newEmpSal'].forEach(id => document.getElementById(id).value = '');
            refreshEmployeeUI();
            alert("✅ Trabajador guardado con éxito.");
        }

        function deleteWorker(id) {
            if(confirm("¿Seguro que deseas eliminar a este trabajador?")) {
                employees = employees.filter(e => e.id !== id);
                localStorage.setItem('AMR_EMPLOYEES', JSON.stringify(employees));
                refreshEmployeeUI();
            }
        }

        function refreshEmployeeUI() {
            const sel = document.getElementById('employeeSelect');
            const listContainer = document.getElementById('workerListContainer');
            
            if(sel && listContainer) {
                sel.innerHTML = '<option value="">Seleccionar Trabajador...</option>';
                listContainer.innerHTML = '';

                employees.forEach(e => { 
                    sel.innerHTML += `<option value="${e.id}">${e.name}</option>`;
                    listContainer.innerHTML += `
                        <div style="display: flex; justify-content: space-between; align-items: center; padding: 4px 8px; border-bottom: 1px solid #e2e8f0; font-size: 11px;">
                            <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap; width: 80%;">${e.name}</span>
                            <span style="color: #ef4444; font-weight: bold; cursor: pointer;" onclick="deleteWorker(${e.id})">🗑️</span>
                        </div>
                    `;
                });
                
                if(employees.length === 0) {
                    listContainer.innerHTML = '<div style="padding: 0.5rem; text-align: center; color: #94a3b8; font-style: italic;">Sin registros</div>';
                }
            }
        }

        function showEmpData() {
            const id = document.getElementById('employeeSelect').value;
            const box = document.getElementById('empDetails');
            if(id) {
                const emp = employees.find(e => e.id == id);
                document.getElementById('detDoc').innerText = emp.doc;
                document.getElementById('detSal').innerText = fmtCur(emp.sal);
                document.getElementById('rawSalary').value = emp.sal;
                box.classList.remove('hidden');
            } else { 
                box.classList.add('hidden'); 
                document.getElementById('rawSalary').value = 0;
            }
            calcVal();
        }

        // --- LÓGICA DE REGISTRO ---
        function updatePeriod() {
            const m = document.getElementById('reportMonth').value;
            const q = document.getElementById('qSelect').value;
            if(!m) return;
            const monthText = new Date(m + "-01").toLocaleString('es-ES', { month: 'long' }).toUpperCase();
            document.getElementById('dispQ1').innerText = `${q}ª QUINCENA`;
            document.getElementById('dispPeriod').innerText = `${q}ª QUINCENA DE ${monthText}`;
            
            const key = `AMR_DATA_${m}_Q${q}`;
            records = JSON.parse(localStorage.getItem(key) || '[]');
            renderTable();
        }

        function addRec() {
            const empId = document.getElementById('employeeSelect').value;
            if(!empId) return alert("⚠️ Seleccione un Colaborador");
            
            const emp = employees.find(x => x.id == empId);
            const novType = document.getElementById('novType').value;
            if(!novType) return alert("⚠️ Seleccione el Tipo de Novedad");

            const incap = document.getElementById('incapPercent').value;

            records.push({
                id: Date.now(), 
                name: emp.name, 
                doc: emp.doc, 
                type: clean(novType),
                incap: clean(incap),
                start: clean(document.getElementById('dateStart').value),
                end: clean(document.getElementById('dateEnd').value),
                days: clean(document.getElementById('dDays').value),
                val: clean(document.getElementById('dVal').value),
                obs: clean(document.getElementById('dObs').value),
                period: `Q${document.getElementById('qSelect').value}`
            });
            
            const m = document.getElementById('reportMonth').value;
            const q = document.getElementById('qSelect').value;
            
            if(!document.getElementById('dispPeriod').innerText.includes("MENSUAL")) {
                localStorage.setItem(`AMR_DATA_${m}_Q${q}`, JSON.stringify(records));
            }
            
            renderTable(); refreshHistoryList();
            
            ['incapPercent','dateStart','dateEnd','dDays','dVal','dObs'].forEach(i => document.getElementById(i).value = '');
            document.getElementById('novType').value = "";
            configFields();
        }

        function renderTable() {
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = '';
            
            if(records.length === 0) {
                tbody.innerHTML = `<tr><td colspan="10" style="padding: 2rem; text-align: center; color: #94a3b8; font-style: italic;">No hay registros para este periodo.</td></tr>`;
                return;
            }

            const currentQ = document.getElementById('qSelect').value;
            if(!document.getElementById('dispPeriod').innerText.includes("MENSUAL")) {
                tbody.innerHTML += `<tr style="background-color: #f8fafc; color: #475569; font-weight: 800; text-align: center; border-top: 2px solid #e2e8f0; border-bottom: 2px solid #e2e8f0;"><td colspan="10" style="padding: 0.5rem;">--- ${currentQ}ª QUINCENA ---</td></tr>`;
            }

            records.forEach(r => {
                if(r.isSeparator) {
                    tbody.innerHTML += `<tr style="background-color: #f8fafc; color: #475569; font-weight: 800; text-align: center; border-top: 2px solid #e2e8f0; border-bottom: 2px solid #e2e8f0;"><td colspan="10" style="padding: 0.5rem;">${r.title}</td></tr>`;
                } else {
                    const money = fmtCur(r.val);
                    const s = (v) => v === "No aplica" ? "txt-red" : "";

                    tbody.innerHTML += `<tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; font-weight: bold; color: #1e293b;">${r.name}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; font-size: 0.75rem;">${r.doc || '---'}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0;" class="${s(r.type)}">${r.type}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; text-align: center; font-weight: bold; color: #d97706;" class="${s(r.incap)}">${r.incap}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; text-align: center; font-size: 9px; color: #64748b;" class="${s(r.start)}">${r.start}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; text-align: center; font-size: 9px; color: #64748b;" class="${s(r.end)}">${r.end}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; text-align: center;" class="${s(r.days)}">${r.days}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; text-align: right; font-weight: bold; color: #4338ca;" class="${s(r.val)}">${renderVal(money)}</td>
                        <td style="padding: 0.75rem; border: 1px solid #e2e8f0; font-size: 9px; font-style: italic; color: #64748b;">${r.obs}</td>
                        <td class="no-print" style="padding: 0.75rem; border: 1px solid #e2e8f0; text-align: center;">
                            <div style="display: flex; justify-content: center; gap: 8px;">
                                <span style="cursor: pointer; font-size: 14px;" onclick="editRow(${r.id})" title="Editar">✏️</span>
                                <span style="cursor: pointer; font-size: 14px;" onclick="deleteRow(${r.id}, '${r.period}')" title="Borrar">🗑️</span>
                            </div>
                        </td>
                    </tr>`;
                }
            });
        }

        // --- LÓGICA DE CAMPOS ---
        function configFields() {
            const type = document.getElementById('novType').value;
            const fStart = document.getElementById('dateStart');
            const fEnd = document.getElementById('dateEnd');
            const fDays = document.getElementById('dDays');
            const fVal = document.getElementById('dVal');
            const fIncap = document.getElementById('incapPercent');
            
            [fStart, fEnd, fDays, fVal].forEach(f => { if(f) { f.disabled = false; f.value = ''; }});
            if(fVal) fVal.readOnly = false;
            if(fIncap) fIncap.value = '';

            if(!type) return;

            if(type.includes('Aumento')) {
                if(fStart) fStart.disabled = true; 
                if(fEnd) fEnd.disabled = true; 
                if(fDays) fDays.disabled = true; 
                if(fIncap) fIncap.value = "No aplica";
            } else if(type.includes('Incapacidad')) {
                if(fVal) fVal.readOnly = true; 
                if(fIncap) fIncap.value = type.includes('ARL') ? '100% (ARL)' : '66.6% (EPS)';
            } else if(['Ingreso Laboral', 'Retiro Laboral'].includes(type)) {
                if(fEnd) fEnd.disabled = true; 
                if(fDays) fDays.disabled = true; 
                if(fVal) { fVal.disabled = true; fVal.value = "No aplica"; } 
                if(fIncap) fIncap.value = "No aplica";
            } else if(type.includes('Remunerado') || type.includes('Vacaciones') || type.includes('Maternidad') || type.includes('Paternidad')) {
                if(fVal) fVal.readOnly = true; 
                if(fIncap) fIncap.value = "No aplica";
            } else if(type.includes('Horas extras') || type.includes('Comisión')) {
                if(fStart) fStart.disabled = true; 
                if(fEnd) fEnd.disabled = true; 
                if(fDays) fDays.disabled = true; 
                if(fVal) fVal.readOnly = false; 
                if(fIncap) fIncap.value = "No aplica";
            } else {
                if(fIncap) fIncap.value = "No aplica";
            }
            calcVal();
        }

        function calcDays() {
            const s = document.getElementById('dateStart').value;
            const e = document.getElementById('dateEnd').value;
            if(s && e) {
                const diff = (new Date(e) - new Date(s)) / (1000 * 60 * 60 * 24);
                const d = diff >= 0 ? diff + 1 : 0;
                document.getElementById('dDays').value = d;
                calcVal();
            }
        }
        
        function calcVal() {
            const type = document.getElementById('novType').value;
            const days = parseFloat(document.getElementById('dDays').value) || 0;
            const salary = parseFloat(document.getElementById('rawSalary').value) || 0;
            if(!type || !days || !salary) return;

            let val = 0;
            if(type.includes('Incapacidad')) {
                 const factor = type.includes('ARL') ? 1 : 0.66666;
                 val = (salary / 30) * days * factor;
            } else if(type.includes('Remunerado') || type.includes('Vacaciones') || type.includes('Maternidad') || type.includes('Paternidad')) {
                 if(!type.includes('NO Remunerado')) {
                    val = (salary / 30) * days;
                 }
            }
            
            if(val > 0) document.getElementById('dVal').value = Math.round(val);
        }

        // --- UTILS & HISTORIAL ---
        function saveConfig() {
            const co = document.getElementById('companyName').value;
            const nit = document.getElementById('companyNIT').value;
            const pr = document.getElementById('preparedBy').value;
            if(document.getElementById('sheetCompanyTitle')) document.getElementById('sheetCompanyTitle').innerText = co || '---';
            if(document.getElementById('sheetCompanyNIT')) document.getElementById('sheetCompanyNIT').innerText = nit || '---';
            if(document.getElementById('dispSign')) document.getElementById('dispSign').innerText = pr || '---';
            localStorage.setItem('amr_co', co); localStorage.setItem('amr_nit', nit); localStorage.setItem('amr_pr', pr);
        }

        function loadSettings() {
            const logo = localStorage.getItem('amr_logo'); if(logo) document.getElementById('sheetLogoBox').innerHTML = `<img src="${logo}" style="height: 75px; width: auto; object-fit: contain;">`;
            const co = localStorage.getItem('amr_co'); if(co) { document.getElementById('companyName').value = co; document.getElementById('sheetCompanyTitle').innerText = co; }
            const nit = localStorage.getItem('amr_nit'); if(nit) { document.getElementById('companyNIT').value = nit; document.getElementById('sheetCompanyNIT').innerText = nit; }
            const pr = localStorage.getItem('amr_pr'); if(pr) { document.getElementById('preparedBy').value = pr; document.getElementById('dispSign').innerText = pr; }
        }

        function handleLogoUpload(i) {
            if(i.files && i.files[0]) {
                const r = new FileReader();
                r.onload = (e) => { 
                    document.getElementById('sheetLogoBox').innerHTML = `<img src="${e.target.result}" style="height: 75px; width: auto; object-fit: contain;">`;
                    localStorage.setItem('amr_logo', e.target.result); 
                };
                r.readAsDataURL(i.files[0]);
            }
        }

        function refreshHistoryList() {
            const list = document.getElementById('historyList'); list.innerHTML = '';
            const keys = Object.keys(localStorage).filter(k => k.startsWith('AMR_DATA_')).sort().reverse();
            [...new Set(keys.map(k => k.substring(9, 16)))].forEach(m => {
                list.innerHTML += `
                <div style="background-color: white; border: 1px solid #e2e8f0; border-radius: 0.25rem; padding: 0.5rem; margin-bottom: 0.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: bold; color: #334155;">${m}</span>
                        <div style="display: flex; gap: 0.5rem;">
                            <button onclick="viewFullMonth('${m}')" style="background-color: #4f46e5; color: white; border: none; padding: 2px 8px; border-radius: 4px; font-size: 9px; font-weight: bold; cursor: pointer;">VER MES</button>
                            <span onclick="deleteMonth('${m}')" style="color: #f43f5e; cursor: pointer; font-size: 14px;" title="Borrar">🗑️</span>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; font-size: 9px; color: #64748b; margin-top: 0.25rem; padding-left: 0.5rem;">
                         <span style="cursor: pointer; text-decoration: underline; color: #4f46e5;" onclick="loadHist('${m}',1)">↳ Ver Q1</span>
                         <span style="cursor: pointer; text-decoration: underline; color: #4f46e5;" onclick="loadHist('${m}',2)">↳ Ver Q2</span>
                    </div>
                </div>`;
            });
        }

        function viewFullMonth(m) {
            const q1 = JSON.parse(localStorage.getItem(`AMR_DATA_${m}_Q1`) || '[]');
            const q2 = JSON.parse(localStorage.getItem(`AMR_DATA_${m}_Q2`) || '[]');
            const sep1 = { isSeparator: true, title: "--- PRIMERA QUINCENA ---" };
            const sep2 = { isSeparator: true, title: "--- SEGUNDA QUINCENA ---" };
            records = [sep1, ...q1, sep2, ...q2];
            document.getElementById('dispPeriod').innerText = `REPORTE MENSUAL: ${m}`;
            document.getElementById('reportMonth').value = m;
            renderTable();
        }

        function deleteMonth(m) {
            if(!confirm(`¿Eliminar historial ${m}?`)) return;
            localStorage.removeItem(`AMR_DATA_${m}_Q1`); localStorage.removeItem(`AMR_DATA_${m}_Q2`);
            refreshHistoryList(); updatePeriod();
        }

        function deleteRow(id, p) {
            if(!confirm("¿Eliminar?")) return;
            const m = document.getElementById('reportMonth').value;
            let cr = JSON.parse(localStorage.getItem(`AMR_DATA_${m}_${p}`) || '[]').filter(r => r.id !== id);
            localStorage.setItem(`AMR_DATA_${m}_${p}`, JSON.stringify(cr));
            if(document.getElementById('dispPeriod').innerText.includes("MENSUAL")) viewFullMonth(m); else updatePeriod();
        }

        function editRow(id) {
            const r = records.find(x => x.id === id);
            if(!r) return;
            const emp = employees.find(e => e.name === r.name);
            if(emp) { document.getElementById('employeeSelect').value = emp.id; showEmpData(); }
            document.getElementById('novType').value = r.type === "No aplica" ? "" : r.type;
            configFields();
            document.getElementById('incapPercent').value = r.incap === "No aplica" ? "" : r.incap;
            document.getElementById('dateStart').value = r.start === "No aplica" ? "" : r.start;
            document.getElementById('dateEnd').value = r.end === "No aplica" ? "" : r.end;
            document.getElementById('dDays').value = r.days === "No aplica" ? "" : r.days;
            document.getElementById('dVal').value = r.val === "No aplica" ? "" : r.val;
            document.getElementById('dObs').value = r.obs || "";
            deleteRow(id, r.period);
        }

        function clearForNew() {
            if(confirm("¿Limpiar vista?")) { records = []; renderTable(); }
        }
        function loadHist(m, q) { document.getElementById('reportMonth').value = m; document.getElementById('qSelect').value = q; updatePeriod(); }

        function generatePDF() {
            const pr = document.getElementById('preparedBy').value;
            if(!pr) return alert("Firma requerida en 'Elaborado por'.");
            
            try {
                const { jsPDF } = window.jspdf; 
                const doc = new jsPDF('l', 'mm', 'a4');
                const logoImg = localStorage.getItem('amr_logo');
                
                if(logoImg) {
                    try {
                        const imgProps = doc.getImageProperties(logoImg);
                        const maxW = 40; const maxH = 20; 
                        let finalW = maxW; let finalH = (imgProps.height * finalW) / imgProps.width;
                        if (finalH > maxH) { finalH = maxH; finalW = (imgProps.width * finalH) / imgProps.height; }
                        doc.addImage(logoImg, 'PNG', 15, 10, finalW, finalH); 
                    } catch(e) {}
                }

                const body = records.map(r => {
                    if(r.isSeparator) return [{ content: r.title, colSpan: 9, styles: { halign: 'center', fillColor: [248, 250, 252], fontStyle: 'bold', textColor: [71, 85, 105] } }];
                    return [
                        r.name, r.doc, r.type, clean(r.incap), clean(r.start), clean(r.end), clean(r.days), fmtCur(r.val), r.obs || ""
                    ];
                });

                doc.autoTable({ 
                    head: [['TRABAJADOR', 'DOC', 'NOVEDAD', '% INCAP', 'INICIO', 'FIN', 'DÍAS', 'VALOR', 'OBSERVACIONES']],
                    body: body, startY: 45, theme: 'grid', styles: { fontSize: 8 },
                    headStyles: { fillColor: [15, 23, 42], textColor: 255 },
                    didParseCell: function(data) {
                        if (data.cell.text[0] === 'No aplica') {
                            data.cell.styles.textColor = [220, 38, 38]; data.cell.styles.fontStyle = 'bold';
                        }
                    },
                    didDrawPage: function (data) {
                        doc.setFontSize(14); doc.setTextColor(99, 102, 241); doc.setFont("helvetica", "bold");
                        doc.text("NOVEDADES DE NÓMINA - SEGURIDAD SOCIAL", 280, 20, { align: 'right' });
                        doc.setFontSize(10); doc.setTextColor(0,0,0);
                        doc.text(document.getElementById('dispPeriod').innerText, 280, 26, { align: 'right' });
                        doc.setFontSize(12); doc.setTextColor(15, 23, 42); 
                        doc.text(document.getElementById('companyName').value || "EMPRESA", 15, 38);
                        doc.setFontSize(9); doc.setFont("helvetica", "normal");
                        doc.text("NIT: " + (document.getElementById('companyNIT').value || "---"), 15, 43);
                        doc.setDrawColor(200, 200, 200); doc.line(15, 44, 280, 44);
                        doc.setFontSize(8); doc.setTextColor(50, 50, 50);
                        doc.text("Elaborado por: " + pr, 15, doc.internal.pageSize.height - 10);
                    }
                });
                doc.save(`AMR_Reporte.pdf`);
            } catch (error) { alert("Error al generar PDF."); }
        }

        function downloadExcel() {
            const wb = XLSX.utils.table_to_book(document.getElementById('mainTable'));
            XLSX.writeFile(wb, `Reporte_AMR.xlsx`);
        }
    </script>
</body>
</html>
