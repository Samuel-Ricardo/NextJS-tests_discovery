import DashboardIndexPage from "@Pages/dashboard";
import "@testing-library/jest-dom";
import {render, screen} from '@testing-library/react'

describe('Dashboard Page', () => {

  it("Shoud render properly", () => {
    render(<DashboardIndexPage/>);

    const header = screen.getByRole('heading');
    const expected = 'Hello World :D'

    expect(header).toHaveTextContent(expected)
  })

  it("Should have a disable button", () => {

    render(<DashboardIndexPage/>)

    const button = screen.getByRole('button')

    expect(button).toBeDisabled();
  })

  it("Should have a <p> Tag with className of blue", () => {
    render(<DashboardIndexPage/>)

    const P = screen.getByTestId('paragraph-blue')
    expect(P).toHaveClass('blue');

    expect(P).toHaveTextContent("Pedro <:()")
  })
})
