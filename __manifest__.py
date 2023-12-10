# -*- coding: utf-8 -*-
{
    'name': "Cuba - Contacts",
    'summary': """Agrega nuevos campos al modulo de contactos con términos usados en Cuba """,
    'description': """
        Agregado nuevos campos a los contactos como:
            - Clave: Identificador único para cada contacto.
            - Abreviatura: Nombre abreviado para identificar los contactos.
            - REEUP: Registro Estatal de Empresas y Unidades Presupuestadas.
            - IRCC: Inscripción en el Registro Comercial de Cuba, CI y NIT.
            - NIT: Número de Identificación Tributaria. (Cambio de string del VAT)
            - CI: Carnet de Identidad
            - Marcar a los contactos asociados a un contacto tipo Individual si es personal autorizado.
            - Agregados campos a la vista árbol de los contactos.
            - En la vista de Contactos en cuanta bancaria se hizo visibles campo de moneda y titular de la cuenta.
    """,
    'author': "José Luis Hernández",
    'website': "https://github.com/theceojose/",
    'category': 'General',
    'version': '1.0',
    'depends': ['base', 'contacts', 'account'],
    'data': [
        'views/res_partner_views.xml',
        'views/account_view_partner_property_form.xml',
        'views/base_view_company_form.xml',
        'views/base_view_partner_tree.xml',
        'views/base_view_partner_bank_tree.xml'
    ],
    'license': 'LGPL-3',
}
