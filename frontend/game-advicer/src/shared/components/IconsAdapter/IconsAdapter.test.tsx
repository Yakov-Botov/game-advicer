import React from 'react';
import { render } from '@testing-library/react';
import {IconsAdapter} from "."

test('Рендеринг IconsAdapter компонента', () => {
    const {container} = render(<IconsAdapter iconType={"IconLikeOutline"} />);
    expect(container).toMatchSnapshot()
})