program ntai
implicit none
real(8) :: t_end, dt, t
real(8), allocatable :: x(:), y(:)
real(8), allocatable :: u(:), v(:)
real(8), allocatable :: x_half(:), y_half(:)
real(8), allocatable :: m(:)
real(8) :: r
integer :: n = 2, i, j
real :: power = 0.75_8
integer :: out_unit = 10  ! 出力用ユニット番号

allocate(x(n), y(n), u(n), v(n), m(n))
allocate(x_half(n), y_half(n))

x = [0.0d0, -2.0d0]
y = [0.0d0, 0.0d0]
u = [0.0d0, 0.0d0]
v = [0.00009d0, -9.0d0]
m = [100.0d0, 0.001d0]

t = 0.0d0
t_end = 10.0d0
dt = 0.002d0

open(unit=out_unit, file='result.dat', status='replace')

! 初期位置の出力
write(out_unit, '(F10.4, 3(2X, F10.6, 2X, F10.6))') t, (x(i), y(i), i=1,n)

do while (t < t_end)
    x_half = x + 0.5d0 * dt * u
    y_half = y + 0.5d0 * dt * v

    do i = 1, n
        do j = 1, n
            if (i /= j) then
                r = sqrt((x_half(i) - x_half(j))**2 + (y_half(i) - y_half(j))**2)
                u(i) = u(i) - 1.0_8 / m(i) * dt * ((m(i) * m(j))/ r ** (power + 1)) * (x_half(i) - x_half(j))
                v(i) = v(i) - 1.0_8 / m(i) * dt * ((m(i) * m(j))/ r ** (power + 1)) * (y_half(i) - y_half(j))
            end if
        end do
    end do

    x = x_half + 0.5d0 * dt * u
    y = y_half + 0.5d0 * dt * v

    t = t + dt

    ! 現在の位置を出力
    write(out_unit, '(F10.4, 3(2X, F10.6, 2X, F10.6))') t, (x(i), y(i), i=1,n)
end do

close(out_unit)

deallocate(x, y, u, v, m)
deallocate(x_half, y_half)
end program ntai
