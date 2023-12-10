from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat = fields.Char(string='NIT', help="El número de identificación fiscal.")
    ci = fields.Char(string='C.I', help="Carnet de Identidad")
    reeup = fields.Char(string='REEUP', help="Registro Estatal de Empresas y Unidades Presupuestadas")
    clave = fields.Char(string='Clave', help="Clave de identificacion única del contacto")
    ircc = fields.Char(string='IRCC', help="Indentificador del Registro Comercial")
    abreviatura = fields.Char(string='Abreviatura', help="Abreviatura del contacto")
    a_personal = fields.Boolean(string="Personal autorizado", help="Es personal autorizado de ese contacto para realizar negocios con ustedes")

    _sql_constraints = [("clave_uniq", "unique(clave)", "Ya existe contacto con esa clave.")]

class Company(models.Model):
    _inherit = "res.company"

    vat = fields.Char(string="NIT")