import DashboardIndexPage from "@/pages/dashboard";
import "@testing-library/jest-dom";
import {render, screen} from '@testing-library/react'

describe('Dashboard page', () => {

  it("Shoud render properly", () => {
    render(<DashboardIndexPage/>);

    const header = screen.getByRole('heading');
    const expected = 'Hello World :D'

    expect(header).toHaveTextContent(expected)
  })
})
