import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WorkersComponent } from './workers/workers.component';
import { OvertimeComponent } from './overtime/overtime.component';

const routes: Routes = [
  { path: 'workers', component: WorkersComponent },
  { path: 'overtime', component: OvertimeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
