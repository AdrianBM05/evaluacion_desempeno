from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación de Desempeño'

    name = fields.Char(string='Título', required=True)
    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True)
    evaluation_date = fields.Date(string='Fecha de Evaluación', required=True)
    comments = fields.Text(string='Comentarios')
    score = fields.Integer(string='Puntuación', required=True, default=1)
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En Proceso'),
        ('done', 'Finalizado')
    ], string='Estado', default='pending')
    
    @api.constrains('score')
    def _check_score(self):
        for record in self:
            if record.score < 1 or record.score > 10:
                raise ValidationError('La puntuación debe estar entre 1 y 10.')