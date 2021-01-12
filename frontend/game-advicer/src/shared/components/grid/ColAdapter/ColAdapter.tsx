import React from 'react'
import { Col, ColProps } from 'react-flexbox-grid'

type ColAdapterProps = ColProps

/** Декоратор над компонентом Col для системы grid приложения */
export const ColAdapter: React.FC<ColAdapterProps> = React.memo((props) => {
    return <Col {...props} />
})