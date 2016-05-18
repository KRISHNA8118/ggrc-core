# Copyright (C) 2016 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: dan@reciprocitylabs.com
# Maintained By: peter@reciprocitylabs.com

"""
remove fields design and operationally

Create Date: 2016-05-18 13:44:51.370427
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '44886d207423'
down_revision = '44ebc240800b'

_table_name = "assessments"
_column_name1 = "design"
_column_name2 = "operationally"

def upgrade():
  """
  Remove design and operationally columns from assessments
  """
  op.drop_column(_table_name, _column_name1)

  op.drop_column(_table_name, _column_name2)


def downgrade():
  """
  Remove design and operationally columns from assessments
  """
  op.add_column(
    _table_name,
    sa.Column(_column_name1, sa.String(length=250), nullable=True)
  )

  op.add_column(
    _table_name,
    sa.Column(_column_name2, sa.String(length=250), nullable=True)
  )

