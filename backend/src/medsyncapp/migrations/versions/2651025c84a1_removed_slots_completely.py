"""removed slots completely

Revision ID: 2651025c84a1
Revises: a6cf7fd5d39b
Create Date: 2023-09-30 20:51:19.674759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2651025c84a1'
down_revision: Union[str, None] = 'a6cf7fd5d39b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ##
    op.drop_constraint('bookings_diagnostic_slot_id_fkey', 'bookings', type_='foreignkey')
    op.drop_constraint('bookings_doctor_slot_id_fkey', 'bookings', type_='foreignkey')#
    op.execute(sa.text("DROP TABLE slots CASCADE"))
    op.drop_table('doctor_slots')
    op.drop_table('diagnostic_slots')
    op.drop_table('doctor_bookings')
    op.add_column('bookings', sa.Column('user_id', sa.BIGINT(), nullable=False))
    op.add_column('bookings', sa.Column('user_message', sa.String(length=1024), nullable=True))
    op.add_column('bookings', sa.Column('doctor_id', sa.Integer(), nullable=True))
    op.add_column('bookings', sa.Column('diagnostic_id', sa.Integer(), nullable=True))
    op.add_column('bookings', sa.Column('location_id', sa.Integer(), nullable=False))
    op.add_column('bookings', sa.Column('booking_time', sa.TIMESTAMP(), nullable=False))
    op.create_foreign_key(None, 'bookings', 'locations', ['location_id'], ['location_id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'bookings', 'diagnostics', ['diagnostic_id'], ['diagnostic_id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'bookings', 'doctors', ['doctor_id'], ['doctor_id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'bookings', 'users', ['user_id'], ['user_id'])
    op.drop_column('bookings', 'doctor_slot_id')
    op.drop_column('bookings', 'diagnostic_slot_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('diagnostic_slot_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('bookings', sa.Column('doctor_slot_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # op.drop_constraint(None, 'bookings', type_='foreignkey')
    # op.drop_constraint(None, 'bookings', type_='foreignkey')
    # op.drop_constraint(None, 'bookings', type_='foreignkey')
    # op.drop_constraint(None, 'bookings', type_='foreignkey')
    op.drop_column('bookings', 'booking_time')
    op.drop_column('bookings', 'location_id')
    op.drop_column('bookings', 'diagnostic_id')
    op.drop_column('bookings', 'doctor_id')
    op.drop_column('bookings', 'user_message')
    op.drop_column('bookings', 'user_id')
    op.create_table('slots',
    sa.Column('slot_id', sa.INTEGER(), server_default=sa.text("nextval('slots_slot_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('location_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('is_booked', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['locations.location_id'], name='slots_location_id_fkey'),
    sa.PrimaryKeyConstraint('slot_id', name='slots_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('diagnostic_slots',
    sa.Column('diagnostic_slot_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('diagnostic_location_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('slot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['diagnostic_location_id'], ['diagnostic_locations.diagnostic_location_id'], name='diagnostic_slots_diagnostic_location_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['slot_id'], ['slots.slot_id'], name='diagnostic_slots_slot_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('diagnostic_slot_id', name='diagnostic_slots_pkey')
    )
    op.create_table('doctor_bookings',
    sa.Column('appointment_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('doctor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('slot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', postgresql.ENUM('Booked', 'Cancelled', name='booking_status', create_type=False), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id'], name='doctor_bookings_doctor_id_fkey'),
    sa.ForeignKeyConstraint(['slot_id'], ['slots.slot_id'], name='doctor_bookings_slot_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='doctor_bookings_user_id_fkey'),
    sa.PrimaryKeyConstraint('appointment_id', name='doctor_bookings_pkey')
    )
    op.create_table('doctor_slots',
    sa.Column('doctor_slot_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('doctor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('slot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id'], name='doctor_slots_doctor_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['slot_id'], ['slots.slot_id'], name='doctor_slots_slot_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('doctor_slot_id', name='doctor_slots_pkey')
    )
    op.create_foreign_key('bookings_doctor_slot_id_fkey', 'bookings', 'doctor_slots', ['doctor_slot_id'], ['doctor_slot_id'], ondelete='CASCADE')
    op.create_foreign_key('bookings_diagnostic_slot_id_fkey', 'bookings', 'diagnostic_slots', ['diagnostic_slot_id'], ['diagnostic_slot_id'], ondelete='CASCADE')
    # ### end Alembic commands ###
